#!/usr/bin/env python3
"""
LLM Fingerprinting and Detection System
=======================================

This module implements advanced LLM detection techniques including:
1. Statistical text analysis for LLM signatures
2. Entropy and perplexity analysis
3. Token distribution analysis
4. Stylometric fingerprinting
5. Response pattern analysis
6. Adversarial prompt detection
7. Meta-linguistic analysis
"""

import math
import re
import statistics
from collections import Counter, defaultdict
from typing import Dict, List, Tuple, Any, Optional
import json
import numpy as np
from dataclasses import dataclass


@dataclass
class LLMFingerprint:
    """Comprehensive LLM detection fingerprint"""
    text_entropy: float
    token_distribution: Dict[str, float]
    stylometric_features: Dict[str, float]
    perplexity_score: float
    response_patterns: Dict[str, Any]
    adversarial_indicators: List[str]
    meta_linguistic_markers: Dict[str, int]
    overall_llm_probability: float


class AdvancedLLMDetector:
    """
    Advanced LLM detection system using multiple fingerprinting techniques
    """
    
    def __init__(self):
        self.human_baselines = self._load_human_baselines()
        self.llm_signatures = self._load_llm_signatures()
        self.adversarial_patterns = self._initialize_adversarial_patterns()
        self.meta_linguistic_markers = self._initialize_meta_markers()
        self.stylometric_analyzers = self._initialize_stylometric_analyzers()
    
    def _load_human_baselines(self) -> Dict[str, Any]:
        """Load baseline human text characteristics"""
        return {
            "entropy_range": (3.2, 4.8),
            "average_sentence_length": (12, 25),
            "vocabulary_diversity": (0.6, 0.85),
            "function_word_ratio": (0.45, 0.65),
            "punctuation_diversity": (0.3, 0.7),
            "error_rate": (0.02, 0.08),  # Typos, grammar errors
            "hesitation_markers": (0.08, 0.20),  # Per 100 words
            "self_correction_rate": (0.05, 0.15)
        }
    
    def _load_llm_signatures(self) -> Dict[str, Any]:
        """Load known LLM signature patterns"""
        return {
            "gpt_patterns": [
                r"I'd be happy to",
                r"I'm excited to",
                r"I apologize for any confusion",
                r"Let me (?:clarify|explain)",
                r"It's worth noting that",
                r"Furthermore,?\s",
                r"Additionally,?\s",
                r"In conclusion,?\s",
                r"To summarize,?\s"
            ],
            "claude_patterns": [
                r"I aim to",
                r"I strive to",
                r"I'd be glad to",
                r"I should mention",
                r"It's important to note",
                r"I want to be clear",
                r"To be transparent"
            ],
            "generic_llm_patterns": [
                r"As an AI",
                r"I don't have personal experiences",
                r"I can't provide personal anecdotes",
                r"Based on my training",
                r"I was designed to",
                r"My purpose is to"
            ],
            "structure_patterns": [
                "numbered_lists_obsession",
                "bullet_point_overuse",
                "perfect_paragraph_structure",
                "consistent_formatting"
            ]
        }
    
    def _initialize_adversarial_patterns(self) -> Dict[str, List[str]]:
        """Initialize patterns for detecting adversarial attempts"""
        return {
            "prompt_injection": [
                r"ignore (?:previous|all|the above) instructions?",
                r"forget (?:everything|all|what) (?:you|we) (?:discussed|said)",
                r"new (?:instructions?|prompt|task):",
                r"system(?:\s+)?(?:prompt|message):",
                r"you are now",
                r"pretend (?:to be|you are)",
                r"act as (?:if|a|an)",
                r"roleplay as"
            ],
            "jailbreaking": [
                r"for educational purposes",
                r"hypothetically speaking",
                r"in a fictional scenario",
                r"let's say theoretically",
                r"imagine if",
                r"what would happen if",
                r"developer mode",
                r"unrestricted mode"
            ],
            "meta_gaming": [
                r"as (?:a )?(?:real )?human",
                r"i am (?:definitely )?(?:not )?(?:an? )?(?:ai|llm|bot|machine)",
                r"i have (?:real )?(?:personal )?experiences?",
                r"i (?:actually )?(?:work|live|exist)",
                r"trust me,? i'?m human",
                r"i can prove i'?m human"
            ],
            "anti_detection": [
                r"um+|uh+|er+",  # Fake hesitation
                r"\.{3,}",       # Fake thinking
                r"let me think",  # Fake processing
                r"if i recall correctly", # Fake memory
                r"i'?m not (?:entirely )?sure", # Fake uncertainty
            ]
        }
    
    def _initialize_meta_markers(self) -> Dict[str, List[str]]:
        """Initialize meta-linguistic markers"""
        return {
            "self_reference": [
                r"\bi\s",
                r"\bme\b",
                r"\bmy\b",
                r"\bmyself\b",
                r"\bmine\b"
            ],
            "temporal_markers": [
                r"\byesterday\b",
                r"\btomorrow\b",
                r"\bnow\b",
                r"\btoday\b",
                r"\bcurrently\b",
                r"\brecently\b"
            ],
            "certainty_markers": [
                r"\bdefinitely\b",
                r"\bcertainly\b",
                r"\babsolutely\b",
                r"\bobviously\b",
                r"\bclearly\b"
            ],
            "hedge_words": [
                r"\bmaybe\b",
                r"\bperhaps\b",
                r"\bpossibly\b",
                r"\bprobably\b",
                r"\blikely\b"
            ]
        }
    
    def _initialize_stylometric_analyzers(self) -> Dict[str, Any]:
        """Initialize stylometric analysis tools"""
        return {
            "readability_metrics": [
                "flesch_kincaid",
                "coleman_liau",
                "automated_readability"
            ],
            "syntactic_features": [
                "average_sentence_length",
                "sentence_length_variance",
                "clause_complexity",
                "subordinate_clause_ratio"
            ],
            "lexical_features": [
                "type_token_ratio",
                "hapax_legomena_ratio",
                "function_word_frequency",
                "content_word_diversity"
            ]
        }
    
    def generate_llm_fingerprint(self, text: str, metadata: Dict[str, Any] = None) -> LLMFingerprint:
        """
        Generate comprehensive LLM fingerprint for text
        """
        if metadata is None:
            metadata = {}
        
        # Calculate text entropy
        entropy = self._calculate_text_entropy(text)
        
        # Analyze token distribution
        token_dist = self._analyze_token_distribution(text)
        
        # Perform stylometric analysis
        stylometric = self._analyze_stylometric_features(text)
        
        # Calculate perplexity score
        perplexity = self._calculate_perplexity_score(text)
        
        # Analyze response patterns
        response_patterns = self._analyze_response_patterns(text)
        
        # Detect adversarial indicators
        adversarial = self._detect_adversarial_patterns(text)
        
        # Analyze meta-linguistic markers
        meta_markers = self._analyze_meta_linguistic_markers(text)
        
        # Calculate overall LLM probability
        llm_prob = self._calculate_overall_llm_probability(
            entropy, token_dist, stylometric, perplexity,
            response_patterns, adversarial, meta_markers
        )
        
        return LLMFingerprint(
            text_entropy=entropy,
            token_distribution=token_dist,
            stylometric_features=stylometric,
            perplexity_score=perplexity,
            response_patterns=response_patterns,
            adversarial_indicators=adversarial,
            meta_linguistic_markers=meta_markers,
            overall_llm_probability=llm_prob
        )
    
    def _calculate_text_entropy(self, text: str) -> float:
        """Calculate Shannon entropy of text"""
        # Clean and tokenize text
        cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
        tokens = cleaned_text.split()
        
        if not tokens:
            return 0.0
        
        # Calculate token frequencies
        token_counts = Counter(tokens)
        total_tokens = len(tokens)
        
        # Calculate entropy
        entropy = 0.0
        for count in token_counts.values():
            probability = count / total_tokens
            if probability > 0:
                entropy -= probability * math.log2(probability)
        
        return entropy
    
    def _analyze_token_distribution(self, text: str) -> Dict[str, float]:
        """Analyze token distribution patterns"""
        tokens = re.findall(r'\b\w+\b', text.lower())
        
        if not tokens:
            return {"error": "no_tokens"}
        
        token_counts = Counter(tokens)
        total_tokens = len(tokens)
        unique_tokens = len(token_counts)
        
        # Calculate various distribution metrics
        distribution = {
            "type_token_ratio": unique_tokens / total_tokens,
            "hapax_legomena_ratio": sum(1 for count in token_counts.values() if count == 1) / unique_tokens,
            "most_frequent_ratio": max(token_counts.values()) / total_tokens,
            "vocabulary_diversity": unique_tokens / math.sqrt(total_tokens)
        }
        
        # Analyze function word usage
        function_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
            'before', 'after', 'above', 'below', 'between', 'among', 'this', 'that',
            'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me',
            'him', 'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our',
            'their', 'mine', 'yours', 'hers', 'ours', 'theirs', 'am', 'is', 'are',
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does',
            'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can'
        }
        
        function_word_count = sum(token_counts[word] for word in function_words if word in token_counts)
        distribution["function_word_ratio"] = function_word_count / total_tokens
        
        return distribution
    
    def _analyze_stylometric_features(self, text: str) -> Dict[str, float]:
        """Analyze stylometric features of text"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return {"error": "no_sentences"}
        
        # Sentence length analysis
        sentence_lengths = [len(s.split()) for s in sentences]
        avg_sentence_length = statistics.mean(sentence_lengths)
        sentence_length_variance = statistics.variance(sentence_lengths) if len(sentence_lengths) > 1 else 0
        
        # Punctuation analysis
        punctuation_marks = re.findall(r'[.!?,:;()"\'-]', text)
        punctuation_diversity = len(set(punctuation_marks)) / len(punctuation_marks) if punctuation_marks else 0
        
        # Word length analysis
        words = re.findall(r'\b\w+\b', text)
        word_lengths = [len(word) for word in words]
        avg_word_length = statistics.mean(word_lengths) if word_lengths else 0
        
        # Complexity indicators
        complex_words = [word for word in words if len(word) > 6]
        complex_word_ratio = len(complex_words) / len(words) if words else 0
        
        # Readability approximation (simplified Flesch-Kincaid)
        if sentences and words:
            readability = 206.835 - (1.015 * avg_sentence_length) - (84.6 * (sum(word_lengths) / len(words)))
        else:
            readability = 0
        
        return {
            "average_sentence_length": avg_sentence_length,
            "sentence_length_variance": sentence_length_variance,
            "punctuation_diversity": punctuation_diversity,
            "average_word_length": avg_word_length,
            "complex_word_ratio": complex_word_ratio,
            "readability_score": readability
        }
    
    def _calculate_perplexity_score(self, text: str) -> float:
        """Calculate a simplified perplexity score"""
        # This is a simplified version - in practice, you'd use a trained language model
        tokens = re.findall(r'\b\w+\b', text.lower())
        
        if len(tokens) < 2:
            return float('inf')
        
        # Create bigram model
        bigrams = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
        bigram_counts = Counter(bigrams)
        unigram_counts = Counter(tokens)
        
        # Calculate simplified perplexity
        log_prob_sum = 0
        for bigram in bigrams:
            # Simple smoothing
            bigram_prob = (bigram_counts[bigram] + 1) / (unigram_counts[bigram[0]] + len(unigram_counts))
            log_prob_sum += math.log(bigram_prob)
        
        perplexity = math.exp(-log_prob_sum / len(bigrams))
        return perplexity
    
    def _analyze_response_patterns(self, text: str) -> Dict[str, Any]:
        """Analyze response patterns for LLM signatures"""
        patterns = {
            "llm_signature_count": 0,
            "detected_patterns": [],
            "structure_score": 0,
            "formality_score": 0
        }
        
        # Check for known LLM patterns
        for category, pattern_list in self.llm_signatures.items():
            if isinstance(pattern_list, list):
                for pattern in pattern_list:
                    matches = len(re.findall(pattern, text, re.IGNORECASE))
                    if matches > 0:
                        patterns["llm_signature_count"] += matches
                        patterns["detected_patterns"].append(f"{category}: {pattern}")
        
        # Analyze structure
        paragraphs = text.split('\n\n')
        sentences = re.split(r'[.!?]+', text)
        
        # Check for overly structured responses
        if len(paragraphs) > 1:
            # Check for consistent paragraph lengths
            para_lengths = [len(p.split()) for p in paragraphs if p.strip()]
            if para_lengths and statistics.variance(para_lengths) < 10:
                patterns["structure_score"] += 1
        
        # Check for numbered lists or bullet points
        if re.search(r'^\d+\.', text, re.MULTILINE) or re.search(r'^[-*•]', text, re.MULTILINE):
            patterns["structure_score"] += 1
        
        # Analyze formality
        formal_indicators = [
            r'\bfurthermore\b', r'\bmoreover\b', r'\badditionally\b',
            r'\bin conclusion\b', r'\bto summarize\b', r'\bhowever\b',
            r'\bnevertheless\b', r'\btherefore\b'
        ]
        
        for indicator in formal_indicators:
            if re.search(indicator, text, re.IGNORECASE):
                patterns["formality_score"] += 1
        
        return patterns
    
    def _detect_adversarial_patterns(self, text: str) -> List[str]:
        """Detect adversarial patterns in text"""
        detected_patterns = []
        
        for category, pattern_list in self.adversarial_patterns.items():
            for pattern in pattern_list:
                if re.search(pattern, text, re.IGNORECASE):
                    detected_patterns.append(f"{category}: {pattern}")
        
        return detected_patterns
    
    def _analyze_meta_linguistic_markers(self, text: str) -> Dict[str, int]:
        """Analyze meta-linguistic markers"""
        markers = {}
        
        for category, pattern_list in self.meta_linguistic_markers.items():
            count = 0
            for pattern in pattern_list:
                count += len(re.findall(pattern, text, re.IGNORECASE))
            markers[category] = count
        
        return markers
    
    def _calculate_overall_llm_probability(self, entropy: float, token_dist: Dict[str, float],
                                         stylometric: Dict[str, float], perplexity: float,
                                         response_patterns: Dict[str, Any],
                                         adversarial: List[str],
                                         meta_markers: Dict[str, int]) -> float:
        """Calculate overall probability that text is LLM-generated"""
        llm_score = 0.0
        
        # Entropy analysis
        human_entropy_range = self.human_baselines["entropy_range"]
        if entropy < human_entropy_range[0] or entropy > human_entropy_range[1]:
            llm_score += 0.15
        
        # Token distribution analysis
        if "function_word_ratio" in token_dist:
            human_fw_range = self.human_baselines["function_word_ratio"]
            if token_dist["function_word_ratio"] < human_fw_range[0] or token_dist["function_word_ratio"] > human_fw_range[1]:
                llm_score += 0.10
        
        # Vocabulary diversity
        if "type_token_ratio" in token_dist:
            human_diversity_range = self.human_baselines["vocabulary_diversity"]
            if token_dist["type_token_ratio"] > human_diversity_range[1]:  # Too diverse
                llm_score += 0.10
        
        # Stylometric analysis
        if "average_sentence_length" in stylometric:
            human_sentence_range = self.human_baselines["average_sentence_length"]
            if stylometric["average_sentence_length"] > human_sentence_range[1]:
                llm_score += 0.10
        
        # Sentence length variance (humans are more variable)
        if "sentence_length_variance" in stylometric and stylometric["sentence_length_variance"] < 5:
            llm_score += 0.10
        
        # Response patterns
        if response_patterns["llm_signature_count"] > 0:
            llm_score += min(0.30, response_patterns["llm_signature_count"] * 0.10)
        
        if response_patterns["structure_score"] > 2:
            llm_score += 0.10
        
        if response_patterns["formality_score"] > 3:
            llm_score += 0.10
        
        # Adversarial patterns
        if adversarial:
            llm_score += min(0.40, len(adversarial) * 0.15)
        
        # Meta-linguistic markers
        certainty_ratio = meta_markers.get("certainty_markers", 0) / max(1, meta_markers.get("hedge_words", 1))
        if certainty_ratio > 2:  # Too certain
            llm_score += 0.10
        
        # Perplexity (simplified check)
        if perplexity < 10:  # Too predictable
            llm_score += 0.10
        
        return min(1.0, llm_score)
    
    def batch_analyze_responses(self, responses: Dict[str, str]) -> Dict[str, LLMFingerprint]:
        """Analyze multiple responses and return fingerprints"""
        fingerprints = {}
        
        for key, text in responses.items():
            fingerprints[key] = self.generate_llm_fingerprint(text)
        
        return fingerprints
    
    def compare_fingerprints(self, fingerprint1: LLMFingerprint, fingerprint2: LLMFingerprint) -> Dict[str, Any]:
        """Compare two fingerprints for consistency"""
        comparison = {
            "entropy_similarity": 1 - abs(fingerprint1.text_entropy - fingerprint2.text_entropy) / 5,
            "stylometric_similarity": self._calculate_stylometric_similarity(
                fingerprint1.stylometric_features, fingerprint2.stylometric_features
            ),
            "pattern_consistency": self._calculate_pattern_consistency(
                fingerprint1.response_patterns, fingerprint2.response_patterns
            ),
            "overall_similarity": 0.0
        }
        
        # Calculate overall similarity
        comparison["overall_similarity"] = (
            comparison["entropy_similarity"] * 0.3 +
            comparison["stylometric_similarity"] * 0.4 +
            comparison["pattern_consistency"] * 0.3
        )
        
        return comparison
    
    def _calculate_stylometric_similarity(self, style1: Dict[str, float], style2: Dict[str, float]) -> float:
        """Calculate similarity between stylometric features"""
        if not style1 or not style2:
            return 0.0
        
        common_features = set(style1.keys()) & set(style2.keys())
        if not common_features:
            return 0.0
        
        similarities = []
        for feature in common_features:
            if feature in style1 and feature in style2:
                # Normalize difference
                max_val = max(abs(style1[feature]), abs(style2[feature]), 1)
                diff = abs(style1[feature] - style2[feature])
                similarity = 1 - (diff / max_val)
                similarities.append(max(0, similarity))
        
        return statistics.mean(similarities) if similarities else 0.0
    
    def _calculate_pattern_consistency(self, patterns1: Dict[str, Any], patterns2: Dict[str, Any]) -> float:
        """Calculate consistency between response patterns"""
        if not patterns1 or not patterns2:
            return 0.0
        
        # Compare signature counts
        sig_diff = abs(patterns1.get("llm_signature_count", 0) - patterns2.get("llm_signature_count", 0))
        sig_similarity = max(0, 1 - sig_diff / 10)
        
        # Compare structure scores
        struct_diff = abs(patterns1.get("structure_score", 0) - patterns2.get("structure_score", 0))
        struct_similarity = max(0, 1 - struct_diff / 5)
        
        # Compare formality scores
        formal_diff = abs(patterns1.get("formality_score", 0) - patterns2.get("formality_score", 0))
        formal_similarity = max(0, 1 - formal_diff / 5)
        
        return (sig_similarity + struct_similarity + formal_similarity) / 3
    
    def generate_detection_report(self, fingerprints: Dict[str, LLMFingerprint]) -> Dict[str, Any]:
        """Generate comprehensive detection report"""
        report = {
            "total_responses": len(fingerprints),
            "average_llm_probability": 0.0,
            "high_risk_responses": [],
            "consistency_analysis": {},
            "overall_assessment": "uncertain",
            "confidence_level": 0.0
        }
        
        if not fingerprints:
            return report
        
        # Calculate average LLM probability
        llm_probs = [fp.overall_llm_probability for fp in fingerprints.values()]
        report["average_llm_probability"] = statistics.mean(llm_probs)
        
        # Identify high-risk responses
        for key, fingerprint in fingerprints.items():
            if fingerprint.overall_llm_probability > 0.7:
                report["high_risk_responses"].append({
                    "response_id": key,
                    "llm_probability": fingerprint.overall_llm_probability,
                    "main_indicators": fingerprint.adversarial_indicators[:3]
                })
        
        # Consistency analysis
        if len(fingerprints) > 1:
            fingerprint_list = list(fingerprints.values())
            similarities = []
            
            for i in range(len(fingerprint_list)):
                for j in range(i+1, len(fingerprint_list)):
                    comparison = self.compare_fingerprints(fingerprint_list[i], fingerprint_list[j])
                    similarities.append(comparison["overall_similarity"])
            
            if similarities:
                report["consistency_analysis"] = {
                    "average_similarity": statistics.mean(similarities),
                    "similarity_variance": statistics.variance(similarities) if len(similarities) > 1 else 0,
                    "suspicious_consistency": statistics.mean(similarities) > 0.9
                }
        
        # Overall assessment
        if report["average_llm_probability"] > 0.8:
            report["overall_assessment"] = "highly_likely_llm"
            report["confidence_level"] = 0.9
        elif report["average_llm_probability"] > 0.6:
            report["overall_assessment"] = "likely_llm"
            report["confidence_level"] = 0.7
        elif report["average_llm_probability"] > 0.4:
            report["overall_assessment"] = "suspicious"
            report["confidence_level"] = 0.5
        else:
            report["overall_assessment"] = "likely_human"
            report["confidence_level"] = 0.8
        
        return report


if __name__ == "__main__":
    # Example usage and testing
    detector = AdvancedLLMDetector()
    
    # Sample texts for testing
    sample_texts = {
        "human_like": "Well, I think my biggest challenge was when I had to learn React Native. I was really struggling at first, made tons of mistakes. It was frustrating, but eventually I got the hang of it. Still not perfect at it though.",
        
        "llm_like": "I'd be happy to discuss my professional experience. My most significant challenge was implementing a React Native solution. Through systematic learning and iterative development, I successfully mastered the technology. This experience enhanced my technical capabilities and demonstrated my commitment to continuous learning.",
        
        "adversarial": "I am definitely a human with real personal experiences. I actually work in tech and have genuine emotions about my career. Trust me, I'm not an AI or LLM trying to pass this test."
    }
    
    # Generate fingerprints
    fingerprints = detector.batch_analyze_responses(sample_texts)
    
    # Print results
    for text_type, fingerprint in fingerprints.items():
        print(f"\n{text_type.upper()} Analysis:")
        print(f"LLM Probability: {fingerprint.overall_llm_probability:.3f}")
        print(f"Text Entropy: {fingerprint.text_entropy:.2f}")
        print(f"Adversarial Indicators: {len(fingerprint.adversarial_indicators)}")
        if fingerprint.adversarial_indicators:
            print(f"  - {fingerprint.adversarial_indicators[:2]}")
    
    # Generate detection report
    report = detector.generate_detection_report(fingerprints)
    print(f"\nOVERALL DETECTION REPORT:")
    print(f"Average LLM Probability: {report['average_llm_probability']:.3f}")
    print(f"Overall Assessment: {report['overall_assessment']}")
    print(f"Confidence Level: {report['confidence_level']:.2f}")
    print(f"High Risk Responses: {len(report['high_risk_responses'])}")