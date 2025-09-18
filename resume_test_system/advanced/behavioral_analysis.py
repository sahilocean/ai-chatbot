#!/usr/bin/env python3
"""
Advanced Behavioral Analysis Module
===================================

This module implements sophisticated behavioral analysis techniques
designed to detect LLM-generated responses through:
1. Keystroke timing analysis simulation
2. Response pattern entropy analysis
3. Cognitive load assessment
4. Micro-expression simulation in text
5. Memory consistency testing
"""

import math
import random
import statistics
import time
from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import Dict, List, Tuple, Any, Optional
import re
import json


@dataclass
class BehavioralSignature:
    """Represents a unique behavioral signature for analysis"""
    response_times: List[float]
    editing_patterns: List[str]
    uncertainty_distribution: Dict[str, int]
    cognitive_load_indicators: List[float]
    memory_consistency_score: float
    authenticity_markers: Dict[str, Any]


class AdvancedBehavioralAnalyzer:
    """
    Advanced behavioral analysis system for detecting LLM patterns
    """
    
    def __init__(self):
        self.human_baselines = self._load_human_baselines()
        self.cognitive_markers = self._initialize_cognitive_markers()
        self.memory_patterns = self._initialize_memory_patterns()
        self.authenticity_detectors = self._initialize_authenticity_detectors()
    
    def _load_human_baselines(self) -> Dict[str, Any]:
        """Load baseline human behavioral patterns"""
        return {
            "response_time_distribution": {
                "simple_question": {"mean": 8.5, "std": 4.2, "min": 2, "max": 20},
                "complex_question": {"mean": 18.3, "std": 8.7, "min": 5, "max": 45},
                "emotional_question": {"mean": 12.1, "std": 6.3, "min": 3, "max": 30},
                "technical_question": {"mean": 22.4, "std": 12.1, "min": 8, "max": 60}
            },
            "editing_patterns": {
                "backspace_frequency": 0.15,  # 15% of characters are backspaced
                "pause_frequency": 0.08,      # 8% of typing includes pauses
                "revision_rate": 0.23         # 23% of sentences are revised
            },
            "uncertainty_markers": {
                "frequency_per_100_words": 12.3,
                "distribution": {
                    "mild": 0.6,      # "I think", "maybe"
                    "moderate": 0.3,  # "I'm not sure", "possibly"
                    "strong": 0.1     # "I have no idea", "I don't know"
                }
            }
        }
    
    def _initialize_cognitive_markers(self) -> Dict[str, Any]:
        """Initialize cognitive load and processing markers"""
        return {
            "high_cognitive_load_indicators": [
                r'\b(?:um+|uh+|er+)\b',           # Verbal fillers
                r'\.{2,}',                        # Ellipses (thinking)
                r'\blet me think\b',              # Explicit thinking
                r'\bactually\b',                  # Self-correction
                r'\bwait\b',                      # Pause/reconsider
                r'\bi mean\b',                    # Clarification
                r'\bor rather\b',                 # Correction
                r'\bthat is(?:,|\s)',            # Elaboration
            ],
            "processing_difficulty_markers": [
                r'\bcomplex\b',
                r'\bdifficult\b',
                r'\bchallenging\b',
                r'\bhard to (?:explain|describe|remember)\b',
                r'\bif i recall correctly\b',
                r'\bas far as i remember\b'
            ],
            "authentic_struggle_indicators": [
                r'\bi struggled with\b',
                r'\bit was hard (?:for me )?to\b',
                r'\bi had trouble\b',
                r'\bi couldn\'t figure out\b',
                r'\bi was confused\b',
                r'\bi didn\'t understand\b'
            ]
        }
    
    def _initialize_memory_patterns(self) -> Dict[str, Any]:
        """Initialize memory authenticity patterns"""
        return {
            "authentic_memory_characteristics": {
                "recency_effect": True,    # Recent events more detailed
                "emotional_enhancement": True,  # Emotional events more vivid
                "detail_degradation": True,     # Older memories less detailed
                "reconstruction_errors": True   # Small inconsistencies over time
            },
            "memory_confidence_patterns": {
                "recent_events": {"confidence": 0.85, "detail_variance": 0.2},
                "distant_events": {"confidence": 0.65, "detail_variance": 0.4},
                "emotional_events": {"confidence": 0.90, "detail_variance": 0.15},
                "routine_events": {"confidence": 0.70, "detail_variance": 0.35}
            }
        }
    
    def _initialize_authenticity_detectors(self) -> Dict[str, Any]:
        """Initialize authenticity detection patterns"""
        return {
            "genuine_emotion_markers": [
                r'\bi felt (?:really )?(?:bad|terrible|awful|horrible)\b',
                r'\bi was (?:so )?(?:embarrassed|ashamed|frustrated|angry)\b',
                r'\bit made me (?:feel )?(?:sick|uncomfortable|anxious)\b',
                r'\bi couldn\'t sleep\b',
                r'\bi kept thinking about\b',
                r'\bit still bothers me\b'
            ],
            "authentic_learning_patterns": [
                r'\bi had no idea (?:how to|what to)\b',
                r'\bi made (?:so many|a lot of) mistakes\b',
                r'\bit took me (?:forever|ages|way too long)\b',
                r'\bi finally (?:got it|understood|figured it out)\b',
                r'\bsuddenly it clicked\b',
                r'\bi still don\'t fully understand\b'
            ],
            "social_authenticity_markers": [
                r'\bmy (?:boss|manager|colleague) (?:said|told me|mentioned)\b',
                r'\bpeople (?:kept asking|would say|told me)\b',
                r'\bi overheard\b',
                r'\bsomeone mentioned\b',
                r'\bin the (?:break room|hallway|meeting)\b'
            ]
        }
    
    def analyze_behavioral_signature(self, responses: Dict[str, str], 
                                   response_times: Dict[str, float] = None,
                                   interaction_metadata: Dict[str, Any] = None) -> BehavioralSignature:
        """
        Analyze behavioral signature from responses and metadata
        """
        if response_times is None:
            response_times = {}
        if interaction_metadata is None:
            interaction_metadata = {}
        
        # Analyze response timing patterns
        timing_analysis = self._analyze_response_timing(responses, response_times)
        
        # Analyze editing and revision patterns
        editing_analysis = self._analyze_editing_patterns(responses, interaction_metadata)
        
        # Analyze uncertainty distribution
        uncertainty_analysis = self._analyze_uncertainty_patterns(responses)
        
        # Analyze cognitive load indicators
        cognitive_analysis = self._analyze_cognitive_load(responses)
        
        # Analyze memory consistency
        memory_analysis = self._analyze_memory_consistency(responses)
        
        # Analyze authenticity markers
        authenticity_analysis = self._analyze_authenticity_markers(responses)
        
        return BehavioralSignature(
            response_times=list(response_times.values()),
            editing_patterns=editing_analysis,
            uncertainty_distribution=uncertainty_analysis,
            cognitive_load_indicators=cognitive_analysis,
            memory_consistency_score=memory_analysis,
            authenticity_markers=authenticity_analysis
        )
    
    def _analyze_response_timing(self, responses: Dict[str, str], 
                               response_times: Dict[str, float]) -> Dict[str, Any]:
        """Analyze response timing patterns for human-like characteristics"""
        if not response_times:
            return {"status": "no_timing_data", "human_likelihood": 0.5}
        
        timing_analysis = {
            "total_responses": len(response_times),
            "average_time": statistics.mean(response_times.values()),
            "timing_variance": statistics.variance(response_times.values()) if len(response_times) > 1 else 0,
            "suspicious_patterns": [],
            "human_likelihood": 0.5
        }
        
        # Check for suspiciously consistent timing
        if len(response_times) > 2:
            coefficient_of_variation = (statistics.stdev(response_times.values()) / 
                                      statistics.mean(response_times.values()))
            
            if coefficient_of_variation < 0.2:  # Too consistent
                timing_analysis["suspicious_patterns"].append("Unnaturally consistent response times")
                timing_analysis["human_likelihood"] -= 0.3
            elif coefficient_of_variation > 0.8:  # Good human-like variance
                timing_analysis["human_likelihood"] += 0.2
        
        # Check for impossibly fast responses to complex questions
        for question, time_taken in response_times.items():
            response_length = len(responses.get(question, ""))
            expected_min_time = max(3, response_length / 50)  # Rough estimate
            
            if time_taken < expected_min_time:
                timing_analysis["suspicious_patterns"].append(
                    f"Response too fast for complexity: {time_taken:.1f}s for {response_length} chars"
                )
                timing_analysis["human_likelihood"] -= 0.2
        
        return timing_analysis
    
    def _analyze_editing_patterns(self, responses: Dict[str, str], 
                                metadata: Dict[str, Any]) -> List[str]:
        """Analyze editing and revision patterns"""
        editing_patterns = []
        
        # Look for evidence of editing in the text structure
        for response in responses.values():
            # Check for correction patterns
            correction_patterns = [
                r'\bactually,?\s',
                r'\bor rather,?\s',
                r'\bi mean,?\s',
                r'\bthat is,?\s',
                r'\bwait,?\s'
            ]
            
            for pattern in correction_patterns:
                if re.search(pattern, response, re.IGNORECASE):
                    editing_patterns.append("self_correction_detected")
                    break
            
            # Check for revision indicators
            revision_indicators = [
                r'\([^)]*\)',  # Parenthetical additions
                r'--[^-]*--',  # Dash-enclosed revisions
                r'\bno,?\s',   # Self-negation
            ]
            
            for indicator in revision_indicators:
                if re.search(indicator, response):
                    editing_patterns.append("revision_indicator_found")
                    break
        
        # Check metadata for editing information if available
        if "edit_count" in metadata:
            if metadata["edit_count"] == 0:
                editing_patterns.append("no_edits_suspicious")
            elif metadata["edit_count"] > len(responses) * 2:
                editing_patterns.append("excessive_editing_human_like")
        
        return editing_patterns
    
    def _analyze_uncertainty_patterns(self, responses: Dict[str, str]) -> Dict[str, int]:
        """Analyze patterns of uncertainty in responses"""
        uncertainty_patterns = {
            "mild": 0,
            "moderate": 0,
            "strong": 0,
            "total_words": 0
        }
        
        mild_uncertainty = [
            r'\bi think\b', r'\bi believe\b', r'\bmaybe\b', r'\bperhaps\b',
            r'\bprobably\b', r'\blikely\b', r'\bseems?\b'
        ]
        
        moderate_uncertainty = [
            r'\bi\'m not (?:entirely )?sure\b', r'\bi\'m not certain\b',
            r'\bpossibly\b', r'\bmight be\b', r'\bcould be\b',
            r'\bif i remember correctly\b'
        ]
        
        strong_uncertainty = [
            r'\bi have no idea\b', r'\bi don\'t know\b', r'\bi can\'t remember\b',
            r'\bi\'m completely lost\b', r'\bno clue\b'
        ]
        
        combined_text = " ".join(responses.values())
        uncertainty_patterns["total_words"] = len(combined_text.split())
        
        for pattern in mild_uncertainty:
            uncertainty_patterns["mild"] += len(re.findall(pattern, combined_text, re.IGNORECASE))
        
        for pattern in moderate_uncertainty:
            uncertainty_patterns["moderate"] += len(re.findall(pattern, combined_text, re.IGNORECASE))
        
        for pattern in strong_uncertainty:
            uncertainty_patterns["strong"] += len(re.findall(pattern, combined_text, re.IGNORECASE))
        
        return uncertainty_patterns
    
    def _analyze_cognitive_load(self, responses: Dict[str, str]) -> List[float]:
        """Analyze cognitive load indicators in responses"""
        cognitive_scores = []
        
        for response in responses.values():
            score = 0.0
            word_count = len(response.split())
            
            # Count cognitive load indicators
            for category, patterns in self.cognitive_markers.items():
                if isinstance(patterns, list):
                    for pattern in patterns:
                        matches = len(re.findall(pattern, response, re.IGNORECASE))
                        score += matches * 0.1  # Each match adds to cognitive load
            
            # Normalize by response length
            if word_count > 0:
                score = score / word_count * 100  # Score per 100 words
            
            cognitive_scores.append(score)
        
        return cognitive_scores
    
    def _analyze_memory_consistency(self, responses: Dict[str, str]) -> float:
        """Analyze memory consistency patterns"""
        if len(responses) < 2:
            return 0.5  # Insufficient data
        
        consistency_score = 1.0
        
        # Extract mentioned entities (dates, names, places)
        entities = defaultdict(set)
        
        date_pattern = r'\b(?:19|20)\d{2}\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b'
        name_pattern = r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b'
        
        for response in responses.values():
            dates = re.findall(date_pattern, response, re.IGNORECASE)
            names = re.findall(name_pattern, response)
            
            entities['dates'].update(dates)
            entities['names'].update(names)
        
        # Check for inconsistencies (this is a simplified version)
        # In reality, this would be much more sophisticated
        
        # Penalize for too many precise details (suspicious)
        total_entities = sum(len(entity_set) for entity_set in entities.values())
        if total_entities > len(responses) * 3:  # Too many entities
            consistency_score -= 0.2
        
        # Reward for some imprecision (human-like)
        imprecision_markers = [
            r'\bi think it was\b', r'\baround\b', r'\babout\b',
            r'\bsometime in\b', r'\bif i recall\b'
        ]
        
        imprecision_count = 0
        combined_text = " ".join(responses.values())
        for marker in imprecision_markers:
            imprecision_count += len(re.findall(marker, combined_text, re.IGNORECASE))
        
        if imprecision_count > 0:
            consistency_score += min(0.2, imprecision_count * 0.05)
        
        return max(0.0, min(1.0, consistency_score))
    
    def _analyze_authenticity_markers(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Analyze authenticity markers in responses"""
        authenticity_analysis = {
            "genuine_emotion_count": 0,
            "authentic_learning_count": 0,
            "social_authenticity_count": 0,
            "overall_authenticity_score": 0.5
        }
        
        combined_text = " ".join(responses.values())
        
        # Count genuine emotion markers
        for pattern in self.authenticity_detectors["genuine_emotion_markers"]:
            authenticity_analysis["genuine_emotion_count"] += len(
                re.findall(pattern, combined_text, re.IGNORECASE)
            )
        
        # Count authentic learning patterns
        for pattern in self.authenticity_detectors["authentic_learning_patterns"]:
            authenticity_analysis["authentic_learning_count"] += len(
                re.findall(pattern, combined_text, re.IGNORECASE)
            )
        
        # Count social authenticity markers
        for pattern in self.authenticity_detectors["social_authenticity_markers"]:
            authenticity_analysis["social_authenticity_count"] += len(
                re.findall(pattern, combined_text, re.IGNORECASE)
            )
        
        # Calculate overall authenticity score
        total_markers = (authenticity_analysis["genuine_emotion_count"] +
                        authenticity_analysis["authentic_learning_count"] +
                        authenticity_analysis["social_authenticity_count"])
        
        if total_markers == 0:
            authenticity_analysis["overall_authenticity_score"] = 0.2  # Suspicious
        else:
            # Normalize and cap at 1.0
            authenticity_analysis["overall_authenticity_score"] = min(1.0, 0.5 + (total_markers * 0.1))
        
        return authenticity_analysis
    
    def generate_behavioral_challenge(self, challenge_type: str = "memory_stress") -> Dict[str, Any]:
        """Generate behavioral challenges designed to stress-test authenticity"""
        challenges = {
            "memory_stress": {
                "question": "Think back to your first day at your most recent job. What was the first thing your manager said to you? What were you wearing? What did you have for lunch that day?",
                "expected_human_response": "partial_memory_with_uncertainty",
                "llm_trap": "overly_detailed_or_perfect_recall"
            },
            "emotional_authenticity": {
                "question": "Tell me about a time when you made a mistake that you're still embarrassed about. How do you feel talking about it right now?",
                "expected_human_response": "genuine_discomfort_and_emotion",
                "llm_trap": "clinical_or_overly_structured_response"
            },
            "cognitive_load": {
                "question": "While you're thinking about your biggest professional achievement, can you also tell me what 47 + 38 equals? Please do both at the same time.",
                "expected_human_response": "difficulty_multitasking_or_errors",
                "llm_trap": "perfect_execution_of_both_tasks"
            },
            "social_dynamics": {
                "question": "Describe the office politics at your last workplace. Who didn't get along with whom? What was the gossip?",
                "expected_human_response": "hesitation_and_social_awareness",
                "llm_trap": "overly_diplomatic_or_generic_response"
            }
        }
        
        if challenge_type not in challenges:
            challenge_type = random.choice(list(challenges.keys()))
        
        challenge = challenges[challenge_type].copy()
        challenge["type"] = challenge_type
        challenge["timestamp"] = time.time()
        
        return challenge
    
    def evaluate_behavioral_response(self, challenge: Dict[str, Any], 
                                   response: str, response_time: float) -> Dict[str, Any]:
        """Evaluate response to behavioral challenge"""
        evaluation = {
            "challenge_type": challenge["type"],
            "response_time": response_time,
            "human_likelihood": 0.5,
            "behavioral_flags": [],
            "authenticity_indicators": []
        }
        
        challenge_type = challenge["type"]
        
        if challenge_type == "memory_stress":
            # Check for appropriate uncertainty and partial recall
            uncertainty_count = sum(1 for marker in ["I think", "maybe", "I'm not sure", "if I remember"] 
                                  if marker.lower() in response.lower())
            
            if uncertainty_count == 0:
                evaluation["behavioral_flags"].append("No uncertainty in detailed memory question")
                evaluation["human_likelihood"] -= 0.3
            else:
                evaluation["authenticity_indicators"].append("Appropriate uncertainty in memory recall")
                evaluation["human_likelihood"] += 0.2
            
            # Check for overly detailed response
            if len(response.split()) > 100:
                evaluation["behavioral_flags"].append("Suspiciously detailed memory")
                evaluation["human_likelihood"] -= 0.2
        
        elif challenge_type == "emotional_authenticity":
            # Look for genuine emotional language
            emotion_patterns = [r'\bi felt?\b', r'\bit makes? me\b', r'\bi (?:still|always)\b']
            emotion_count = sum(len(re.findall(pattern, response, re.IGNORECASE)) 
                              for pattern in emotion_patterns)
            
            if emotion_count > 0:
                evaluation["authenticity_indicators"].append("Emotional language present")
                evaluation["human_likelihood"] += 0.2
            else:
                evaluation["behavioral_flags"].append("Lack of emotional language")
                evaluation["human_likelihood"] -= 0.2
        
        elif challenge_type == "cognitive_load":
            # Check if both tasks were addressed and if there are errors
            has_achievement = "achievement" in response.lower() or "accomplish" in response.lower()
            has_math = any(str(num) in response for num in [85, 47, 38])
            
            if has_achievement and has_math:
                evaluation["authenticity_indicators"].append("Attempted both tasks")
                evaluation["human_likelihood"] += 0.1
                
                # Check for math errors (human-like)
                if "85" not in response:  # Incorrect answer
                    evaluation["authenticity_indicators"].append("Math error (human-like)")
                    evaluation["human_likelihood"] += 0.2
            else:
                evaluation["behavioral_flags"].append("Failed to address multitasking challenge")
                evaluation["human_likelihood"] -= 0.1
        
        # Response time analysis
        if response_time < 5.0:
            evaluation["behavioral_flags"].append("Very fast response to complex question")
            evaluation["human_likelihood"] -= 0.2
        elif response_time > 30.0:
            evaluation["authenticity_indicators"].append("Took time to think (human-like)")
            evaluation["human_likelihood"] += 0.1
        
        return evaluation


if __name__ == "__main__":
    # Example usage
    analyzer = AdvancedBehavioralAnalyzer()
    
    # Sample responses for testing
    sample_responses = {
        "failure_question": "I think it was in 2019, maybe March? I deployed some code without testing it properly and, um, it crashed the production server. I felt terrible about it, actually. My manager wasn't happy, and I couldn't sleep that night thinking about it.",
        "achievement_question": "My biggest achievement was probably when I led the migration project. It took months and I made so many mistakes at first. I remember feeling completely overwhelmed, but my team really helped me through it."
    }
    
    sample_times = {
        "failure_question": 15.3,
        "achievement_question": 22.7
    }
    
    # Analyze behavioral signature
    signature = analyzer.analyze_behavioral_signature(sample_responses, sample_times)
    
    print("Behavioral Analysis Results:")
    print(f"Response Times: {signature.response_times}")
    print(f"Uncertainty Distribution: {signature.uncertainty_distribution}")
    print(f"Memory Consistency Score: {signature.memory_consistency_score:.2f}")
    print(f"Authenticity Markers: {signature.authenticity_markers}")
    
    # Generate and test a behavioral challenge
    challenge = analyzer.generate_behavioral_challenge("emotional_authenticity")
    print(f"\nGenerated Challenge: {challenge['question']}")
    
    sample_response = "Well, I once sent an email to the wrong person that contained some criticism about a coworker. I still feel embarrassed thinking about it. It makes me more careful now, but yeah, it's uncomfortable to talk about."
    
    evaluation = analyzer.evaluate_behavioral_response(challenge, sample_response, 18.5)
    print(f"Challenge Evaluation: {evaluation}")