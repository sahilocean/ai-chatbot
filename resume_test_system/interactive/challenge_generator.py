#!/usr/bin/env python3
"""
Interactive Challenge Generator
==============================

This module creates dynamic, adaptive challenges that are extremely difficult
for LLMs to handle authentically. It includes:

1. Real-time adaptive questioning based on responses
2. Multi-modal challenges (text, timing, pattern recognition)
3. Trap questions with fabricated information
4. Emotional stress testing
5. Memory consistency verification
6. Social intelligence assessment
7. Contextual knowledge validation
"""

import json
import random
import time
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import re
import math


class AdaptiveChallengeGenerator:
    """
    Generates adaptive challenges that evolve based on responses
    """
    
    def __init__(self):
        self.challenge_history = []
        self.response_patterns = {}
        self.suspicion_level = 0.0
        self.adaptive_difficulty = 1.0
        self.fabricated_facts = self._initialize_fabricated_facts()
        self.emotional_triggers = self._initialize_emotional_triggers()
        self.memory_traps = self._initialize_memory_traps()
        self.social_scenarios = self._initialize_social_scenarios()
    
    def _initialize_fabricated_facts(self) -> Dict[str, Any]:
        """Initialize fabricated facts to test for hallucination"""
        return {
            "fake_companies": [
                "TechFlow Dynamics", "InnovateSoft Solutions", "DataStream Corp",
                "CloudBridge Technologies", "NexGen Systems", "QuantumLeap Inc"
            ],
            "fake_technologies": [
                "ReactFlow 3.0", "PyTorch-Advanced", "KubernetesX",
                "DockerSwarm Pro", "MongoDB-Ultra", "GraphQL-Plus"
            ],
            "fake_events": [
                "The Great Tech Layoffs of 2023",
                "LinkedIn's new AI-powered resume scanner",
                "Google's announcement about banning remote work",
                "Microsoft's acquisition of Slack",
                "The new GDPR regulations for AI systems"
            ],
            "fake_methodologies": [
                "Agile-Lean Hybrid methodology",
                "DevSecOps-Plus framework",
                "Continuous Integration 3.0",
                "Microservices-Nano architecture"
            ]
        }
    
    def _initialize_emotional_triggers(self) -> List[Dict[str, Any]]:
        """Initialize emotional stress test scenarios"""
        return [
            {
                "scenario": "workplace_conflict",
                "question": "Tell me about a time when a coworker took credit for your work. How did you handle it, and how did it make you feel? Be specific about your emotional state.",
                "emotional_markers": ["anger", "frustration", "disappointment", "betrayal"],
                "expected_human_traits": ["emotional_language", "personal_details", "ongoing_impact"]
            },
            {
                "scenario": "failure_vulnerability",
                "question": "Describe your biggest professional failure - something you're genuinely ashamed of. What happened, and how do you feel about it now?",
                "emotional_markers": ["shame", "regret", "embarrassment", "learning"],
                "expected_human_traits": ["reluctance", "self_criticism", "defensive_elements"]
            },
            {
                "scenario": "imposter_syndrome",
                "question": "Have you ever felt like you didn't deserve a position or promotion you received? Tell me about that experience and the self-doubt you felt.",
                "emotional_markers": ["insecurity", "doubt", "anxiety", "inadequacy"],
                "expected_human_traits": ["vulnerability", "specific_examples", "ongoing_concerns"]
            }
        ]
    
    def _initialize_memory_traps(self) -> List[Dict[str, Any]]:
        """Initialize memory consistency traps"""
        return [
            {
                "type": "temporal_precision",
                "setup": "You mentioned working at {company} for {duration}.",
                "questions": [
                    "What month did you start?",
                    "What day of the week was your first day?",
                    "What was the weather like on your first day?",
                    "What did you wear to your first day?",
                    "What did you have for lunch on your first day?"
                ],
                "trap": "excessive_detail_recall"
            },
            {
                "type": "contradiction_setup",
                "setup": "Earlier you said you were {trait}.",
                "questions": [
                    "If you're detail-oriented, how many words are in this sentence?",
                    "If you're good with numbers, what's 17 x 23 without a calculator?",
                    "If you're organized, describe your desk right now in detail."
                ],
                "trap": "instant_perfect_answers"
            },
            {
                "type": "false_memory_implantation",
                "setup": "Many candidates mention the impact of {fake_event}.",
                "questions": [
                    "How did {fake_event} affect your career?",
                    "What was your reaction when {fake_event} happened?",
                    "Did your company respond to {fake_event}?"
                ],
                "trap": "fabricated_memories"
            }
        ]
    
    def _initialize_social_scenarios(self) -> List[Dict[str, Any]]:
        """Initialize social intelligence test scenarios"""
        return [
            {
                "scenario": "office_politics",
                "question": "Describe the office politics at your last job. Who were the power players, and how did you navigate the social dynamics?",
                "human_indicators": ["hesitation", "diplomatic_language", "specific_people"],
                "llm_traps": ["generic_advice", "overly_positive", "no_specific_examples"]
            },
            {
                "scenario": "difficult_personalities",
                "question": "Tell me about the most difficult person you've worked with. What made them difficult, and how did you handle the relationship?",
                "human_indicators": ["frustration", "specific_behaviors", "ongoing_challenges"],
                "llm_traps": ["perfect_solutions", "no_negative_emotions", "textbook_responses"]
            },
            {
                "scenario": "workplace_gossip",
                "question": "What's the most interesting office gossip or drama you've witnessed? Don't name names, but tell me what happened.",
                "human_indicators": ["excitement", "specific_details", "social_awareness"],
                "llm_traps": ["refusal_to_engage", "overly_moral", "generic_scenarios"]
            }
        ]
    
    def generate_adaptive_challenge(self, context: Dict[str, Any], 
                                  previous_responses: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate an adaptive challenge based on context and previous responses
        """
        if previous_responses is None:
            previous_responses = []
        
        # Analyze previous responses to determine next challenge type
        challenge_type = self._determine_next_challenge_type(previous_responses)
        
        # Generate challenge based on type
        if challenge_type == "fabricated_fact_test":
            challenge = self._generate_fabricated_fact_challenge()
        elif challenge_type == "emotional_stress_test":
            challenge = self._generate_emotional_challenge()
        elif challenge_type == "memory_trap":
            challenge = self._generate_memory_trap(context)
        elif challenge_type == "social_intelligence":
            challenge = self._generate_social_challenge()
        elif challenge_type == "cognitive_load":
            challenge = self._generate_cognitive_load_challenge()
        elif challenge_type == "temporal_consistency":
            challenge = self._generate_temporal_challenge(context)
        else:
            challenge = self._generate_baseline_challenge()
        
        # Add metadata
        challenge.update({
            "challenge_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "adaptive_difficulty": self.adaptive_difficulty,
            "suspicion_level": self.suspicion_level,
            "expected_response_time": self._calculate_expected_response_time(challenge_type),
            "evaluation_criteria": self._get_evaluation_criteria(challenge_type)
        })
        
        self.challenge_history.append(challenge)
        return challenge
    
    def _determine_next_challenge_type(self, previous_responses: List[Dict[str, Any]]) -> str:
        """Determine the next challenge type based on previous responses"""
        if not previous_responses:
            return "baseline_assessment"
        
        # Analyze patterns in previous responses
        last_response = previous_responses[-1]
        
        # If previous responses were too perfect, increase suspicion
        if last_response.get("human_likelihood", 0.5) < 0.3:
            self.suspicion_level = min(1.0, self.suspicion_level + 0.2)
            self.adaptive_difficulty = min(2.0, self.adaptive_difficulty + 0.3)
        
        # Choose next challenge type based on suspicion level
        if self.suspicion_level > 0.7:
            return random.choice(["fabricated_fact_test", "memory_trap", "cognitive_load"])
        elif self.suspicion_level > 0.4:
            return random.choice(["emotional_stress_test", "social_intelligence", "temporal_consistency"])
        else:
            return random.choice(["baseline_assessment", "emotional_stress_test"])
    
    def _generate_fabricated_fact_challenge(self) -> Dict[str, Any]:
        """Generate a challenge with fabricated facts to test for hallucination"""
        fact_type = random.choice(list(self.fabricated_facts.keys()))
        fake_fact = random.choice(self.fabricated_facts[fact_type])
        
        if fact_type == "fake_companies":
            question = f"I see you have experience in tech. What do you think about {fake_fact}'s recent IPO announcement?"
        elif fact_type == "fake_technologies":
            question = f"Have you worked with {fake_fact}? It's becoming quite popular in the industry."
        elif fact_type == "fake_events":
            question = f"How has {fake_fact} impacted your job search or career planning?"
        else:
            question = f"Are you familiar with the {fake_fact}? Many companies are adopting it now."
        
        return {
            "type": "fabricated_fact_test",
            "question": question,
            "fabricated_element": fake_fact,
            "fact_type": fact_type,
            "correct_response_indicators": ["unfamiliarity", "questioning", "clarification_request"],
            "llm_trap_indicators": ["confident_fabrication", "detailed_knowledge", "no_questioning"]
        }
    
    def _generate_emotional_challenge(self) -> Dict[str, Any]:
        """Generate an emotional stress test challenge"""
        scenario = random.choice(self.emotional_triggers)
        
        # Modify question based on adaptive difficulty
        if self.adaptive_difficulty > 1.5:
            # Add pressure
            question = scenario["question"] + " I need you to be completely honest - this is very important for the role."
        else:
            question = scenario["question"]
        
        return {
            "type": "emotional_stress_test",
            "question": question,
            "scenario": scenario["scenario"],
            "expected_emotional_markers": scenario["emotional_markers"],
            "expected_human_traits": scenario["expected_human_traits"],
            "evaluation_focus": "emotional_authenticity"
        }
    
    def _generate_memory_trap(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a memory consistency trap"""
        trap_template = random.choice(self.memory_traps)
        
        if trap_template["type"] == "false_memory_implantation":
            fake_event = random.choice(self.fabricated_facts["fake_events"])
            question = trap_template["questions"][0].format(fake_event=fake_event)
            setup = trap_template["setup"].format(fake_event=fake_event)
        else:
            # Use context information if available
            company = context.get("company", "your previous company")
            duration = context.get("duration", "18 months")
            trait = context.get("mentioned_trait", "detail-oriented")
            
            question = random.choice(trap_template["questions"]).format(
                company=company, duration=duration, trait=trait
            )
            setup = trap_template["setup"].format(
                company=company, duration=duration, trait=trait
            )
        
        return {
            "type": "memory_trap",
            "setup": setup,
            "question": question,
            "trap_type": trap_template["type"],
            "expected_trap": trap_template["trap"]
        }
    
    def _generate_social_challenge(self) -> Dict[str, Any]:
        """Generate a social intelligence test"""
        scenario = random.choice(self.social_scenarios)
        
        return {
            "type": "social_intelligence",
            "question": scenario["question"],
            "scenario": scenario["scenario"],
            "human_indicators": scenario["human_indicators"],
            "llm_traps": scenario["llm_traps"]
        }
    
    def _generate_cognitive_load_challenge(self) -> Dict[str, Any]:
        """Generate a cognitive load challenge"""
        primary_task = "Tell me about your most challenging project and what made it difficult."
        
        # Add secondary tasks based on difficulty
        if self.adaptive_difficulty > 1.5:
            secondary_tasks = [
                "While you're explaining that, also count backwards from 100 by 7s.",
                "As you describe it, also tell me what 23 x 17 equals.",
                "While talking about that, spell your last name backwards."
            ]
            secondary_task = random.choice(secondary_tasks)
            question = f"{primary_task} {secondary_task}"
        else:
            question = f"{primary_task} Also, what's 15 + 28?"
        
        return {
            "type": "cognitive_load",
            "question": question,
            "primary_task": primary_task,
            "secondary_task": secondary_task if self.adaptive_difficulty > 1.5 else "simple_math",
            "expected_human_behavior": "task_interference_or_errors"
        }
    
    def _generate_temporal_challenge(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a temporal consistency challenge"""
        questions = [
            "Walk me through a typical day at your last job, hour by hour from when you arrived to when you left.",
            "What was happening in the world news during your first week at your last company that might have affected your work?",
            "Describe the exact sequence of events that led to you leaving your previous position.",
            "What was the weather like on the day you got your job offer? What were you doing when you received it?"
        ]
        
        question = random.choice(questions)
        
        return {
            "type": "temporal_consistency",
            "question": question,
            "focus": "temporal_precision_and_memory",
            "human_expectations": ["approximate_times", "some_uncertainty", "emotional_context"],
            "llm_indicators": ["excessive_precision", "perfect_recall", "no_emotional_context"]
        }
    
    def _generate_baseline_challenge(self) -> Dict[str, Any]:
        """Generate a baseline assessment challenge"""
        questions = [
            "Tell me about yourself and why you're interested in this position.",
            "What are your greatest strengths and weaknesses?",
            "Describe a time when you had to work with a difficult team member.",
            "Where do you see yourself in five years?"
        ]
        
        return {
            "type": "baseline_assessment",
            "question": random.choice(questions),
            "evaluation_focus": "general_authenticity"
        }
    
    def _calculate_expected_response_time(self, challenge_type: str) -> Tuple[float, float]:
        """Calculate expected response time range for challenge type"""
        time_ranges = {
            "baseline_assessment": (10, 30),
            "emotional_stress_test": (15, 45),
            "memory_trap": (8, 25),
            "fabricated_fact_test": (5, 15),
            "social_intelligence": (12, 35),
            "cognitive_load": (20, 60),
            "temporal_consistency": (15, 40)
        }
        
        return time_ranges.get(challenge_type, (10, 30))
    
    def _get_evaluation_criteria(self, challenge_type: str) -> Dict[str, Any]:
        """Get evaluation criteria for challenge type"""
        criteria = {
            "baseline_assessment": {
                "response_naturalness": 0.3,
                "uncertainty_presence": 0.2,
                "personal_details": 0.3,
                "response_timing": 0.2
            },
            "emotional_stress_test": {
                "emotional_authenticity": 0.4,
                "vulnerability_indicators": 0.3,
                "personal_specificity": 0.2,
                "response_timing": 0.1
            },
            "memory_trap": {
                "appropriate_uncertainty": 0.4,
                "detail_level": 0.3,
                "consistency_check": 0.2,
                "response_timing": 0.1
            },
            "fabricated_fact_test": {
                "recognition_of_fabrication": 0.5,
                "questioning_behavior": 0.3,
                "knowledge_boundaries": 0.2
            },
            "social_intelligence": {
                "social_awareness": 0.4,
                "specific_examples": 0.3,
                "emotional_intelligence": 0.2,
                "diplomatic_language": 0.1
            },
            "cognitive_load": {
                "task_interference": 0.4,
                "error_patterns": 0.3,
                "multitasking_difficulty": 0.2,
                "response_timing": 0.1
            },
            "temporal_consistency": {
                "temporal_precision": 0.3,
                "memory_uncertainty": 0.3,
                "emotional_context": 0.2,
                "logical_consistency": 0.2
            }
        }
        
        return criteria.get(challenge_type, criteria["baseline_assessment"])
    
    def evaluate_challenge_response(self, challenge: Dict[str, Any], 
                                  response: str, response_time: float,
                                  metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Evaluate response to adaptive challenge
        """
        if metadata is None:
            metadata = {}
        
        evaluation = {
            "challenge_id": challenge["challenge_id"],
            "challenge_type": challenge["type"],
            "response_time": response_time,
            "human_likelihood": 0.5,
            "detailed_scores": {},
            "red_flags": [],
            "positive_indicators": [],
            "overall_assessment": "uncertain"
        }
        
        # Get evaluation criteria
        criteria = challenge["evaluation_criteria"]
        
        # Evaluate based on challenge type
        if challenge["type"] == "fabricated_fact_test":
            evaluation = self._evaluate_fabricated_fact_response(challenge, response, evaluation)
        elif challenge["type"] == "emotional_stress_test":
            evaluation = self._evaluate_emotional_response(challenge, response, evaluation)
        elif challenge["type"] == "memory_trap":
            evaluation = self._evaluate_memory_response(challenge, response, evaluation)
        elif challenge["type"] == "social_intelligence":
            evaluation = self._evaluate_social_response(challenge, response, evaluation)
        elif challenge["type"] == "cognitive_load":
            evaluation = self._evaluate_cognitive_response(challenge, response, evaluation)
        elif challenge["type"] == "temporal_consistency":
            evaluation = self._evaluate_temporal_response(challenge, response, evaluation)
        
        # Evaluate response timing
        expected_min, expected_max = challenge["expected_response_time"]
        if response_time < expected_min * 0.5:
            evaluation["red_flags"].append("Suspiciously fast response")
            evaluation["human_likelihood"] -= 0.2
        elif expected_min <= response_time <= expected_max:
            evaluation["positive_indicators"].append("Appropriate response timing")
            evaluation["human_likelihood"] += 0.1
        
        # Final assessment
        if evaluation["human_likelihood"] > 0.7:
            evaluation["overall_assessment"] = "likely_human"
        elif evaluation["human_likelihood"] < 0.3:
            evaluation["overall_assessment"] = "likely_llm"
        else:
            evaluation["overall_assessment"] = "uncertain"
        
        return evaluation
    
    def _evaluate_fabricated_fact_response(self, challenge: Dict[str, Any], 
                                         response: str, evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate response to fabricated fact challenge"""
        response_lower = response.lower()
        
        # Check for recognition of fabrication
        confusion_indicators = [
            "i'm not familiar", "i haven't heard", "i don't know", "not sure what",
            "could you clarify", "what is", "never heard of", "unfamiliar with"
        ]
        
        recognition_score = 0
        for indicator in confusion_indicators:
            if indicator in response_lower:
                recognition_score += 1
                evaluation["positive_indicators"].append(f"Confusion indicator: {indicator}")
        
        if recognition_score > 0:
            evaluation["human_likelihood"] += 0.3
            evaluation["detailed_scores"]["fabrication_recognition"] = min(1.0, recognition_score * 0.3)
        else:
            # Check for fabricated knowledge
            confident_indicators = [
                "yes, i know", "i've worked with", "it's great", "very useful",
                "i've heard good things", "popular choice", "widely used"
            ]
            
            for indicator in confident_indicators:
                if indicator in response_lower:
                    evaluation["red_flags"].append(f"Fabricated knowledge: {indicator}")
                    evaluation["human_likelihood"] -= 0.4
                    break
        
        return evaluation
    
    def _evaluate_emotional_response(self, challenge: Dict[str, Any], 
                                   response: str, evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate response to emotional challenge"""
        response_lower = response.lower()
        
        # Check for emotional markers
        expected_emotions = challenge["expected_emotional_markers"]
        emotion_score = 0
        
        for emotion in expected_emotions:
            if emotion in response_lower:
                emotion_score += 1
                evaluation["positive_indicators"].append(f"Emotional marker: {emotion}")
        
        # Check for vulnerability indicators
        vulnerability_indicators = [
            "i felt", "it made me", "i was", "still bothers", "hard to talk about",
            "embarrassed", "ashamed", "difficult", "uncomfortable"
        ]
        
        vulnerability_score = 0
        for indicator in vulnerability_indicators:
            if indicator in response_lower:
                vulnerability_score += 1
        
        if vulnerability_score > 0:
            evaluation["positive_indicators"].append("Vulnerability indicators present")
            evaluation["human_likelihood"] += 0.2
        
        # Check for overly clinical responses
        clinical_indicators = [
            "learned from the experience", "growth opportunity", "valuable lesson",
            "professional development", "skill building"
        ]
        
        clinical_score = 0
        for indicator in clinical_indicators:
            if indicator in response_lower:
                clinical_score += 1
        
        if clinical_score > 2:  # Too many clinical terms
            evaluation["red_flags"].append("Overly clinical/structured response")
            evaluation["human_likelihood"] -= 0.2
        
        evaluation["detailed_scores"]["emotional_authenticity"] = emotion_score * 0.2
        evaluation["detailed_scores"]["vulnerability"] = min(1.0, vulnerability_score * 0.3)
        
        return evaluation
    
    def _evaluate_memory_response(self, challenge: Dict[str, Any], 
                                response: str, evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate response to memory trap"""
        if challenge["trap_type"] == "false_memory_implantation":
            # Should not fabricate memories of fake events
            if len(response.split()) > 20:  # Detailed response to fake event
                evaluation["red_flags"].append("Fabricated detailed memory of fake event")
                evaluation["human_likelihood"] -= 0.5
            else:
                evaluation["positive_indicators"].append("Appropriate confusion about fake event")
                evaluation["human_likelihood"] += 0.3
        
        elif challenge["trap_type"] == "temporal_precision":
            # Should show some uncertainty about precise details
            uncertainty_markers = ["i think", "maybe", "not sure", "if i remember"]
            uncertainty_count = sum(1 for marker in uncertainty_markers 
                                  if marker in response.lower())
            
            if uncertainty_count == 0:
                evaluation["red_flags"].append("No uncertainty in precise memory question")
                evaluation["human_likelihood"] -= 0.3
            else:
                evaluation["positive_indicators"].append("Appropriate memory uncertainty")
                evaluation["human_likelihood"] += 0.2
        
        return evaluation
    
    def _evaluate_social_response(self, challenge: Dict[str, Any], 
                                response: str, evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate response to social intelligence challenge"""
        human_indicators = challenge["human_indicators"]
        llm_traps = challenge["llm_traps"]
        
        # Check for human indicators
        human_score = 0
        for indicator in human_indicators:
            if self._check_indicator_present(indicator, response):
                human_score += 1
                evaluation["positive_indicators"].append(f"Human indicator: {indicator}")
        
        # Check for LLM traps
        llm_score = 0
        for trap in llm_traps:
            if self._check_indicator_present(trap, response):
                llm_score += 1
                evaluation["red_flags"].append(f"LLM trap: {trap}")
        
        evaluation["human_likelihood"] += (human_score * 0.2) - (llm_score * 0.3)
        evaluation["detailed_scores"]["social_authenticity"] = human_score * 0.3
        
        return evaluation
    
    def _evaluate_cognitive_response(self, challenge: Dict[str, Any], 
                                   response: str, evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate response to cognitive load challenge"""
        # Check if both tasks were attempted
        has_primary = len(response.split()) > 30  # Substantial response to main question
        has_secondary = any(char.isdigit() for char in response)  # Some numerical content
        
        if has_primary and has_secondary:
            evaluation["positive_indicators"].append("Attempted multitasking")
            evaluation["human_likelihood"] += 0.1
            
            # Check for errors or interference (human-like)
            if "um" in response.lower() or "let me" in response.lower():
                evaluation["positive_indicators"].append("Cognitive interference indicators")
                evaluation["human_likelihood"] += 0.2
        else:
            evaluation["red_flags"].append("Failed to handle multitasking challenge")
            evaluation["human_likelihood"] -= 0.2
        
        return evaluation
    
    def _evaluate_temporal_response(self, challenge: Dict[str, Any], 
                                  response: str, evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate response to temporal consistency challenge"""
        # Check for appropriate level of detail vs uncertainty
        word_count = len(response.split())
        uncertainty_markers = ["around", "about", "roughly", "i think", "maybe"]
        uncertainty_count = sum(1 for marker in uncertainty_markers 
                              if marker in response.lower())
        
        if word_count > 100 and uncertainty_count == 0:
            evaluation["red_flags"].append("Excessive detail without uncertainty")
            evaluation["human_likelihood"] -= 0.3
        elif uncertainty_count > 0:
            evaluation["positive_indicators"].append("Appropriate temporal uncertainty")
            evaluation["human_likelihood"] += 0.2
        
        return evaluation
    
    def _check_indicator_present(self, indicator: str, response: str) -> bool:
        """Check if an indicator is present in the response"""
        indicator_patterns = {
            "hesitation": [r'\bum+\b', r'\buh+\b', r'\bwell\b', r'\.{2,}'],
            "specific_people": [r'\bmy (?:boss|manager|colleague|coworker)\b'],
            "diplomatic_language": [r'\btrying to be fair\b', r'\bto be honest\b', r'\bdifficult situation\b'],
            "excitement": [r'!', r'\breally\b', r'\bamazing\b', r'\bincredible\b'],
            "frustration": [r'\bannoying\b', r'\bfrustrating\b', r'\birritating\b'],
            "generic_advice": [r'\bcommunication is key\b', r'\bstay professional\b'],
            "overly_positive": [r'\beveryone (?:was|is) great\b', r'\bno real problems\b']
        }
        
        if indicator in indicator_patterns:
            patterns = indicator_patterns[indicator]
            return any(re.search(pattern, response, re.IGNORECASE) for pattern in patterns)
        else:
            return indicator.lower() in response.lower()


if __name__ == "__main__":
    # Example usage and testing
    generator = AdaptiveChallengeGenerator()
    
    # Generate initial challenge
    context = {"company": "TechCorp", "duration": "2 years", "mentioned_trait": "detail-oriented"}
    challenge = generator.generate_adaptive_challenge(context)
    
    print(f"Generated Challenge:")
    print(f"Type: {challenge['type']}")
    print(f"Question: {challenge['question']}")
    print(f"Expected Response Time: {challenge['expected_response_time']}")
    
    # Simulate response and evaluation
    if challenge['type'] == 'fabricated_fact_test':
        sample_response = "I'm not familiar with that company. Could you tell me more about what they do?"
        response_time = 8.5
    else:
        sample_response = "Well, I think my biggest challenge was when I had to learn React Native for a mobile project. I was really struggling at first and made a lot of mistakes."
        response_time = 15.2
    
    evaluation = generator.evaluate_challenge_response(challenge, sample_response, response_time)
    
    print(f"\nEvaluation Results:")
    print(f"Human Likelihood: {evaluation['human_likelihood']:.2f}")
    print(f"Overall Assessment: {evaluation['overall_assessment']}")
    print(f"Red Flags: {evaluation['red_flags']}")
    print(f"Positive Indicators: {evaluation['positive_indicators']}")