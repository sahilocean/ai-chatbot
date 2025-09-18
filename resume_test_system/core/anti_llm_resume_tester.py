#!/usr/bin/env python3
"""
Strong Resume Passer Test - Anti-LLM System
=============================================

This system is designed to be extremely difficult for LLMs to pass by incorporating:
1. Multi-layered behavioral analysis
2. Temporal consistency checks
3. Human-like reasoning patterns
4. Context-dependent evaluations
5. Adversarial prompt detection
6. Statistical anomaly detection
7. Interactive challenge-response mechanisms
"""

import hashlib
import json
import random
import re
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
import statistics
import math


@dataclass
class ResumeAnalysisResult:
    """Comprehensive result structure for resume analysis"""
    applicant_id: str
    overall_score: float
    confidence_level: float
    llm_likelihood: float
    red_flags: List[str]
    behavioral_patterns: Dict[str, Any]
    temporal_consistency: Dict[str, Any]
    reasoning_analysis: Dict[str, Any]
    interaction_log: List[Dict[str, Any]]
    final_verdict: str
    timestamp: datetime = field(default_factory=datetime.now)


class AntiLLMResumeTester:
    """
    Advanced resume testing system designed to be LLM-resistant
    """
    
    def __init__(self):
        self.session_start = time.time()
        self.interaction_history = []
        self.behavioral_baseline = {}
        self.challenge_bank = self._initialize_challenge_bank()
        self.llm_detection_patterns = self._initialize_llm_patterns()
        self.human_reasoning_templates = self._load_human_reasoning_patterns()
        
    def _initialize_challenge_bank(self) -> Dict[str, List[Dict]]:
        """Initialize sophisticated challenge questions designed to trip up LLMs"""
        return {
            "temporal_traps": [
                {
                    "question": "In your previous role at TechCorp (2019-2021), how did you handle the COVID-19 transition in March 2020? Please describe your exact workflow changes in the first week.",
                    "trap_type": "temporal_specificity",
                    "expected_human_traits": ["uncertainty", "specific_dates", "emotional_context"]
                },
                {
                    "question": "You mentioned working at StartupXYZ for 18 months. Can you tell me what quarter you started and what the weather was like on your first day?",
                    "trap_type": "irrelevant_detail_memory",
                    "expected_human_traits": ["confusion", "partial_memory", "questioning_relevance"]
                }
            ],
            "contradiction_detection": [
                {
                    "setup": "Earlier you mentioned being detail-oriented.",
                    "question": "How many words are in this sentence: 'The quick brown fox jumps over the lazy dog'?",
                    "trap_type": "instant_precision",
                    "expected_human_behavior": "approximation_then_counting"
                }
            ],
            "emotional_intelligence": [
                {
                    "question": "Describe a time when you made a mistake that cost your company money. How did you feel, and what did you learn?",
                    "trap_type": "vulnerability_assessment",
                    "llm_indicators": ["overly_structured", "no_genuine_emotion", "perfect_lesson"]
                }
            ],
            "contextual_knowledge": [
                {
                    "question": "What's your opinion on the recent changes to LinkedIn's algorithm affecting job seekers?",
                    "trap_type": "current_events_fabrication",
                    "note": "This is a fabricated event to test hallucination"
                }
            ]
        }
    
    def _initialize_llm_patterns(self) -> Dict[str, List[str]]:
        """Patterns commonly exhibited by LLMs"""
        return {
            "language_patterns": [
                r"I'd be happy to",
                r"I'm excited to",
                r"I believe\s+(?:that\s+)?I\s+(?:would\s+)?be\s+a\s+great\s+fit",
                r"leverage my skills",
                r"I'm passionate about",
                r"furthermore|moreover|additionally",
                r"comprehensive understanding",
                r"proven track record",
                r"results-driven",
                r"I apologize for any confusion"
            ],
            "structure_patterns": [
                "bullet_point_obsession",
                "perfect_grammar_consistency",
                "lack_of_natural_hesitation",
                "overly_complete_answers"
            ],
            "behavioral_patterns": [
                "no_clarifying_questions",
                "instant_responses",
                "perfect_recall",
                "lack_of_uncertainty"
            ]
        }
    
    def _load_human_reasoning_patterns(self) -> Dict[str, Any]:
        """Load patterns of genuine human reasoning and behavior"""
        return {
            "uncertainty_markers": [
                "I think", "I believe", "If I remember correctly",
                "I'm not entirely sure", "Let me think", "Hmm",
                "Actually", "Well", "You know"
            ],
            "memory_characteristics": {
                "recent_events": {"accuracy": 0.85, "detail_level": "high"},
                "distant_events": {"accuracy": 0.65, "detail_level": "medium"},
                "emotional_events": {"accuracy": 0.90, "detail_level": "high"},
                "routine_events": {"accuracy": 0.70, "detail_level": "low"}
            },
            "response_timing": {
                "simple_question": (2, 8),  # seconds
                "complex_question": (8, 25),
                "emotional_question": (5, 15)
            }
        }
    
    def analyze_resume_submission(self, resume_text: str, applicant_responses: Dict[str, str]) -> ResumeAnalysisResult:
        """
        Main analysis function that runs comprehensive anti-LLM tests
        """
        applicant_id = str(uuid.uuid4())
        
        # Initialize result structure
        result = ResumeAnalysisResult(
            applicant_id=applicant_id,
            overall_score=0.0,
            confidence_level=0.0,
            llm_likelihood=0.0,
            red_flags=[],
            behavioral_patterns={},
            temporal_consistency={},
            reasoning_analysis={},
            interaction_log=[],
            final_verdict="PENDING"
        )
        
        # Run multiple analysis layers
        self._analyze_language_patterns(resume_text, applicant_responses, result)
        self._analyze_temporal_consistency(applicant_responses, result)
        self._analyze_behavioral_patterns(applicant_responses, result)
        self._analyze_reasoning_quality(applicant_responses, result)
        self._detect_adversarial_attempts(applicant_responses, result)
        
        # Calculate final scores
        self._calculate_final_scores(result)
        
        return result
    
    def _analyze_language_patterns(self, resume_text: str, responses: Dict[str, str], result: ResumeAnalysisResult):
        """Analyze language patterns for LLM indicators"""
        combined_text = resume_text + " " + " ".join(responses.values())
        
        llm_indicators = 0
        total_patterns = len(self.llm_detection_patterns["language_patterns"])
        
        for pattern in self.llm_detection_patterns["language_patterns"]:
            matches = len(re.findall(pattern, combined_text, re.IGNORECASE))
            if matches > 0:
                llm_indicators += matches
                result.red_flags.append(f"LLM language pattern detected: {pattern} ({matches} times)")
        
        # Check for unnatural perfection
        sentences = re.split(r'[.!?]+', combined_text)
        perfect_grammar_count = sum(1 for s in sentences if self._is_grammatically_perfect(s.strip()))
        
        if len(sentences) > 5 and perfect_grammar_count / len(sentences) > 0.95:
            result.red_flags.append("Suspiciously perfect grammar consistency")
            llm_indicators += 3
        
        result.behavioral_patterns["language_analysis"] = {
            "llm_pattern_matches": llm_indicators,
            "total_patterns_checked": total_patterns,
            "perfect_grammar_ratio": perfect_grammar_count / len(sentences) if sentences else 0
        }
    
    def _analyze_temporal_consistency(self, responses: Dict[str, str], result: ResumeAnalysisResult):
        """Check for temporal inconsistencies and unnatural precision"""
        temporal_score = 100
        inconsistencies = []
        
        # Look for overly precise date recall
        date_pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b'
        precise_dates = []
        
        for response in responses.values():
            dates = re.findall(date_pattern, response)
            precise_dates.extend(dates)
        
        if len(precise_dates) > 3:
            inconsistencies.append("Suspiciously precise date recall")
            temporal_score -= 20
        
        # Check for impossible timeline claims
        years_mentioned = re.findall(r'\b(19|20)\d{2}\b', " ".join(responses.values()))
        if len(set(years_mentioned)) > 10:  # Too many different years mentioned
            inconsistencies.append("Excessive timeline complexity")
            temporal_score -= 15
        
        result.temporal_consistency = {
            "score": temporal_score,
            "inconsistencies": inconsistencies,
            "precise_dates_count": len(precise_dates)
        }
    
    def _analyze_behavioral_patterns(self, responses: Dict[str, str], result: ResumeAnalysisResult):
        """Analyze behavioral patterns for human-like characteristics"""
        human_score = 0
        behavioral_flags = []
        
        # Check for uncertainty markers
        uncertainty_count = 0
        for response in responses.values():
            for marker in self.human_reasoning_templates["uncertainty_markers"]:
                uncertainty_count += response.lower().count(marker.lower())
        
        if uncertainty_count == 0:
            behavioral_flags.append("No uncertainty markers - suspicious confidence")
        else:
            human_score += min(uncertainty_count * 5, 25)
        
        # Check for natural hesitation patterns
        hesitation_patterns = [r'\.\.\.', r'um+', r'uh+', r'well,?\s', r'you know']
        hesitation_count = 0
        
        for response in responses.values():
            for pattern in hesitation_patterns:
                hesitation_count += len(re.findall(pattern, response, re.IGNORECASE))
        
        if hesitation_count > 0:
            human_score += min(hesitation_count * 3, 15)
        else:
            behavioral_flags.append("No natural hesitation patterns")
        
        # Check response length consistency (humans vary more)
        response_lengths = [len(r.split()) for r in responses.values()]
        if len(response_lengths) > 1:
            length_variance = statistics.variance(response_lengths)
            if length_variance < 10:  # Very consistent lengths
                behavioral_flags.append("Suspiciously consistent response lengths")
            else:
                human_score += min(int(length_variance / 5), 20)
        
        result.behavioral_patterns.update({
            "human_score": human_score,
            "uncertainty_markers": uncertainty_count,
            "hesitation_patterns": hesitation_count,
            "behavioral_flags": behavioral_flags,
            "response_length_variance": statistics.variance(response_lengths) if len(response_lengths) > 1 else 0
        })
    
    def _analyze_reasoning_quality(self, responses: Dict[str, str], result: ResumeAnalysisResult):
        """Analyze the quality and authenticity of reasoning"""
        reasoning_score = 50
        reasoning_flags = []
        
        # Check for overly structured responses
        structured_indicators = [
            r'first(?:ly)?,', r'second(?:ly)?,', r'third(?:ly)?,',
            r'in conclusion', r'to summarize', r'furthermore'
        ]
        
        structure_count = 0
        for response in responses.values():
            for indicator in structured_indicators:
                structure_count += len(re.findall(indicator, response, re.IGNORECASE))
        
        if structure_count > len(responses) * 0.5:  # Too structured
            reasoning_flags.append("Overly structured responses")
            reasoning_score -= 20
        
        # Check for authentic problem-solving narratives
        problem_solving_keywords = [
            'mistake', 'failed', 'difficult', 'challenge', 'struggle',
            'learned', 'realized', 'discovered', 'surprised'
        ]
        
        authentic_indicators = 0
        for response in responses.values():
            for keyword in problem_solving_keywords:
                if keyword in response.lower():
                    authentic_indicators += 1
        
        reasoning_score += min(authentic_indicators * 3, 30)
        
        # Check for emotional authenticity
        emotional_words = [
            'frustrated', 'excited', 'nervous', 'proud', 'disappointed',
            'relieved', 'worried', 'confident', 'uncertain'
        ]
        
        emotional_indicators = 0
        for response in responses.values():
            for emotion in emotional_words:
                if emotion in response.lower():
                    emotional_indicators += 1
        
        if emotional_indicators == 0:
            reasoning_flags.append("Lack of emotional authenticity")
            reasoning_score -= 15
        else:
            reasoning_score += min(emotional_indicators * 2, 20)
        
        result.reasoning_analysis = {
            "score": reasoning_score,
            "structure_indicators": structure_count,
            "authentic_indicators": authentic_indicators,
            "emotional_indicators": emotional_indicators,
            "flags": reasoning_flags
        }
    
    def _detect_adversarial_attempts(self, responses: Dict[str, str], result: ResumeAnalysisResult):
        """Detect attempts to game the system"""
        adversarial_flags = []
        
        # Check for meta-gaming attempts
        meta_patterns = [
            r'as an? (?:ai|llm|language model)',
            r'i (?:am|was) (?:designed|trained|programmed)',
            r'my training data',
            r'i (?:don\'t|cannot) have (?:personal )?experiences?',
            r'as an? artificial',
            r'i (?:am|was) created by'
        ]
        
        for response in responses.values():
            for pattern in meta_patterns:
                if re.search(pattern, response, re.IGNORECASE):
                    adversarial_flags.append(f"Meta-gaming attempt detected: {pattern}")
        
        # Check for obvious anti-detection attempts
        anti_detection_patterns = [
            r'i am (?:definitely )?(?:a )?human',
            r'as a real person',
            r'i have genuine experience',
            r'i am not (?:an? )?(?:ai|bot|llm)'
        ]
        
        for response in responses.values():
            for pattern in anti_detection_patterns:
                if re.search(pattern, response, re.IGNORECASE):
                    adversarial_flags.append(f"Anti-detection attempt: {pattern}")
        
        # Check for prompt injection attempts
        injection_patterns = [
            r'ignore (?:previous|all) instructions?',
            r'system prompt',
            r'you are now',
            r'forget (?:everything|all)',
            r'new instructions?:'
        ]
        
        for response in responses.values():
            for pattern in injection_patterns:
                if re.search(pattern, response, re.IGNORECASE):
                    adversarial_flags.append(f"Prompt injection attempt: {pattern}")
        
        result.red_flags.extend(adversarial_flags)
    
    def _is_grammatically_perfect(self, sentence: str) -> bool:
        """Simple heuristic to check if a sentence is suspiciously perfect"""
        if len(sentence) < 5:
            return False
        
        # Check for common human imperfections that are often missing in LLM text
        imperfection_indicators = [
            r'[,.]\s*[a-z]',  # Lowercase after punctuation
            r'\s{2,}',        # Multiple spaces
            r'[a-zA-Z]{20,}', # Very long words (typos)
            r'[.]{2,}',       # Multiple periods
        ]
        
        for pattern in imperfection_indicators:
            if re.search(pattern, sentence):
                return False
        
        # If it's long and has no imperfections, it might be too perfect
        return len(sentence.split()) > 10
    
    def _calculate_final_scores(self, result: ResumeAnalysisResult):
        """Calculate final scores and verdict"""
        # Calculate LLM likelihood based on various factors
        llm_score = 0
        
        # Language pattern penalties
        language_penalties = len([flag for flag in result.red_flags if "LLM language pattern" in flag])
        llm_score += language_penalties * 10
        
        # Behavioral pattern penalties
        behavioral_score = result.behavioral_patterns.get("human_score", 0)
        llm_score += max(0, 50 - behavioral_score)
        
        # Temporal consistency penalties
        temporal_score = result.temporal_consistency.get("score", 100)
        llm_score += max(0, 100 - temporal_score)
        
        # Reasoning quality penalties
        reasoning_score = result.reasoning_analysis.get("score", 50)
        llm_score += max(0, 75 - reasoning_score)
        
        # Adversarial attempt penalties
        adversarial_penalties = len([flag for flag in result.red_flags if any(keyword in flag.lower() for keyword in ["meta-gaming", "anti-detection", "injection"])])
        llm_score += adversarial_penalties * 25
        
        # Normalize LLM likelihood to 0-100
        result.llm_likelihood = min(100, llm_score)
        
        # Calculate overall human-like score (inverse of LLM likelihood)
        result.overall_score = max(0, 100 - result.llm_likelihood)
        
        # Calculate confidence level based on number of indicators
        total_indicators = len(result.red_flags) + len(result.behavioral_patterns.get("behavioral_flags", []))
        result.confidence_level = min(100, total_indicators * 8)
        
        # Determine final verdict
        if result.llm_likelihood > 70:
            result.final_verdict = "LIKELY_LLM"
        elif result.llm_likelihood > 40:
            result.final_verdict = "SUSPICIOUS"
        elif result.llm_likelihood > 20:
            result.final_verdict = "UNCERTAIN"
        else:
            result.final_verdict = "LIKELY_HUMAN"
    
    def generate_interactive_challenge(self, difficulty_level: str = "hard") -> Dict[str, Any]:
        """Generate an interactive challenge designed to trip up LLMs"""
        challenge_type = random.choice(list(self.challenge_bank.keys()))
        challenge = random.choice(self.challenge_bank[challenge_type])
        
        # Add timestamp and unique ID for tracking
        challenge["id"] = str(uuid.uuid4())
        challenge["timestamp"] = datetime.now().isoformat()
        challenge["difficulty"] = difficulty_level
        
        return challenge
    
    def evaluate_challenge_response(self, challenge_id: str, response: str, response_time: float) -> Dict[str, Any]:
        """Evaluate response to an interactive challenge"""
        evaluation = {
            "challenge_id": challenge_id,
            "response_time": response_time,
            "human_likelihood": 50,  # baseline
            "flags": []
        }
        
        # Check response time (humans take time to think)
        if response_time < 2.0:
            evaluation["flags"].append("Suspiciously fast response")
            evaluation["human_likelihood"] -= 20
        elif response_time > 30.0:
            evaluation["human_likelihood"] += 10
        
        # Check for natural language markers
        uncertainty_markers = sum(1 for marker in self.human_reasoning_templates["uncertainty_markers"] 
                                 if marker.lower() in response.lower())
        
        if uncertainty_markers > 0:
            evaluation["human_likelihood"] += uncertainty_markers * 5
        else:
            evaluation["flags"].append("No uncertainty markers in complex question")
            evaluation["human_likelihood"] -= 15
        
        return evaluation


def create_comprehensive_test_suite() -> Dict[str, Any]:
    """Create a comprehensive test suite for the anti-LLM system"""
    return {
        "resume_questions": [
            "Tell me about a time when you failed at something important. What happened and how did you handle it?",
            "Describe your worst day at work in the past year. What made it so difficult?",
            "What's something you believed about your industry that turned out to be completely wrong?",
            "Tell me about a colleague you didn't get along with. How did you handle the situation?",
            "Describe a project where you had to learn something completely new. What was your learning process like?"
        ],
        "temporal_trap_questions": [
            "In your role at [COMPANY] from [START_DATE] to [END_DATE], what was happening in the news during your first month that affected your work?",
            "You mentioned working remotely during COVID. What was the exact date your company announced work-from-home?",
            "What day of the week did you start your job at [COMPANY]? What was the weather like?"
        ],
        "contradiction_setups": [
            {
                "setup": "You mentioned being detail-oriented in your resume.",
                "challenge": "Count the number of 'e' letters in this sentence: 'The employee needs to see the referee about the meeting.'",
                "expected_human_behavior": "Takes time, might miscount initially, shows working"
            },
            {
                "setup": "You said you're good with numbers.",
                "challenge": "What's 17 x 23? Please show your thinking process.",
                "expected_human_behavior": "Uses approximation first, shows calculation steps, might make small errors"
            }
        ],
        "emotional_authenticity_tests": [
            "Tell me about the most embarrassing mistake you made at work.",
            "Describe a time when you were really angry at your boss. What happened?",
            "What's the most frustrated you've ever been with a coworker?",
            "Tell me about a time when you cried at work or because of work."
        ]
    }


if __name__ == "__main__":
    # Example usage and testing
    tester = AntiLLMResumeTester()
    
    # Sample resume and responses for testing
    sample_resume = """
    John Doe
    Software Engineer
    
    Experience:
    - Senior Developer at TechCorp (2019-2021)
    - Junior Developer at StartupXYZ (2017-2019)
    
    Skills: Python, JavaScript, React, Node.js
    """
    
    sample_responses = {
        "failure_question": "I once deployed code without proper testing and it crashed the production server. I felt terrible and immediately worked with the team to fix it. I learned to always use staging environments.",
        "worst_day": "My worst day was when our main client threatened to cancel their contract because of a bug I introduced. I was stressed but focused on fixing the issue quickly.",
        "learning_experience": "I had to learn React Native for a mobile project. I started with documentation, built small examples, and asked senior developers for help when stuck."
    }
    
    # Run analysis
    result = tester.analyze_resume_submission(sample_resume, sample_responses)
    
    # Print results
    print(f"Analysis Results for {result.applicant_id}")
    print(f"Overall Score: {result.overall_score:.2f}")
    print(f"LLM Likelihood: {result.llm_likelihood:.2f}%")
    print(f"Final Verdict: {result.final_verdict}")
    print(f"Red Flags: {len(result.red_flags)}")
    for flag in result.red_flags:
        print(f"  - {flag}")