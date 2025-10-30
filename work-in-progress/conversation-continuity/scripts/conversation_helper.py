#!/usr/bin/env python3
"""
Conversation Continuity Helper Script

Author: Colin Bitterfield
Email: colin@bitterfield.com
Date Created: 2025-10-30
Date Updated: 2025-10-30
Version: 1.0.0

This script provides utilities for the conversation-continuity skill:
- Calculate memory pressure scores
- Initialize knowledge base files
- Create handover templates
- Validate knowledge base structure
"""

import yaml
import json
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path
import sys


def calculate_memory_score(message_count: int, tool_call_count: int) -> int:
    """
    Calculate memory pressure score.
    
    Formula: (messages * 1) + (tool_calls * 2)
    Thresholds: Warn at 50, Critical at 70
    
    Args:
        message_count: Number of messages in conversation
        tool_call_count: Number of tool calls made
        
    Returns:
        Memory pressure score (0-100+)
    """
    return (message_count * 1) + (tool_call_count * 2)


def get_memory_status(score: int) -> Dict[str, any]:
    """
    Get memory status based on score.
    
    Args:
        score: Memory pressure score
        
    Returns:
        Dictionary with status, level, and recommendation
    """
    if score < 50:
        return {
            "status": "healthy",
            "level": "green",
            "recommendation": "Continue normally"
        }
    elif score < 70:
        return {
            "status": "warning",
            "level": "yellow",
            "recommendation": "Consider preparing handover soon"
        }
    else:
        return {
            "status": "critical",
            "level": "red",
            "recommendation": "Prepare handover immediately"
        }


def init_knowledge_base(project_path: str, 
                        versioning_preference: str = "internal") -> Dict:
    """
    Initialize a new knowledge base structure.
    
    Args:
        project_path: Absolute path to project root
        versioning_preference: "internal" or "filename"
        
    Returns:
        Dictionary with knowledge base structure
    """
    now = datetime.utcnow().isoformat() + 'Z'
    
    knowledge_base = {
        "version": "1.0.0",
        "last_updated": now,
        "versioning_preference": versioning_preference,
        "created_date": now,
        "project_path": project_path,
        "first_run_message_shown": False,
        
        "questions_answered": [],
        "decisions": [],
        
        "capabilities": {
            "last_checked": now,
            "tools_available": [],
            "extensions_available": [],
            "workspace_type": "unknown",
            "filesystem_access": {
                "project_directory": project_path,
                "workspace_directory": "/home/claude",
                "access_level": "unknown"
            },
            "mcp_servers": [],
            "known_limitations": []
        },
        
        "conflicts_resolved": [],
        "context_snapshots": [],
        
        "statistics": {
            "total_conversations": 0,
            "total_questions": 0,
            "total_decisions": 0,
            "total_conflicts": 0,
            "total_snapshots": 0,
            "total_handovers": 0,
            "most_asked_questions": [],
            "most_active_categories": [],
            "average_conversation_length": 0.0,
            "average_tool_calls": 0.0,
            "last_handover": None,
            "last_conflict": None,
            "health_metrics": {
                "knowledge_growth_rate": 0.0,
                "question_repeat_rate": 0.0,
                "conflict_rate": 0.0,
                "handover_frequency": 0.0
            }
        }
    }
    
    return knowledge_base


def save_knowledge_base(knowledge_base: Dict, filepath: str) -> bool:
    """
    Save knowledge base to YAML file.
    
    Args:
        knowledge_base: Knowledge base dictionary
        filepath: Path to save file
        
    Returns:
        True if successful
    """
    try:
        with open(filepath, 'w') as f:
            yaml.safe_dump(knowledge_base, f, 
                          default_flow_style=False,
                          sort_keys=False,
                          allow_unicode=True)
        return True
    except Exception as e:
        print(f"Error saving knowledge base: {e}", file=sys.stderr)
        return False


def load_knowledge_base(filepath: str) -> Optional[Dict]:
    """
    Load knowledge base from YAML file.
    
    Args:
        filepath: Path to knowledge base file
        
    Returns:
        Knowledge base dictionary or None if error
    """
    try:
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Knowledge base not found: {filepath}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error loading knowledge base: {e}", file=sys.stderr)
        return None


def validate_knowledge_base(knowledge_base: Dict) -> List[str]:
    """
    Validate knowledge base structure.
    
    Args:
        knowledge_base: Knowledge base dictionary
        
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    # Check required top-level fields
    required_fields = [
        "version", "last_updated", "versioning_preference",
        "created_date", "project_path", "questions_answered",
        "decisions", "capabilities", "conflicts_resolved",
        "context_snapshots", "statistics"
    ]
    
    for field in required_fields:
        if field not in knowledge_base:
            errors.append(f"Missing required field: {field}")
    
    # Validate capabilities structure
    if "capabilities" in knowledge_base:
        cap_required = ["last_checked", "tools_available", 
                       "extensions_available", "workspace_type"]
        for field in cap_required:
            if field not in knowledge_base["capabilities"]:
                errors.append(f"Missing capabilities field: {field}")
    
    # Validate statistics structure
    if "statistics" in knowledge_base:
        stat_required = ["total_conversations", "total_questions",
                        "total_decisions", "total_conflicts"]
        for field in stat_required:
            if field not in knowledge_base["statistics"]:
                errors.append(f"Missing statistics field: {field}")
    
    return errors


def add_question(knowledge_base: Dict, question: str, answer: str,
                category: str) -> Dict:
    """
    Add a question to the knowledge base.
    
    Args:
        knowledge_base: Knowledge base dictionary
        question: The question asked
        answer: The answer provided
        category: Question category
        
    Returns:
        Updated knowledge base
    """
    now = datetime.utcnow().isoformat() + 'Z'
    
    # Generate simple ID
    q_count = len(knowledge_base["questions_answered"]) + 1
    q_id = f"q{q_count:03d}"
    
    question_entry = {
        "id": q_id,
        "question": question,
        "answer": answer,
        "category": category,
        "first_asked": now,
        "last_asked": now,
        "times_asked": 1,
        "variations": [],
        "related_decisions": [],
        "tags": []
    }
    
    knowledge_base["questions_answered"].append(question_entry)
    knowledge_base["statistics"]["total_questions"] += 1
    knowledge_base["last_updated"] = now
    
    return knowledge_base


def add_decision(knowledge_base: Dict, decision: str, rationale: str,
                category: str, scope: str = "project",
                confidence: str = "medium") -> Dict:
    """
    Add a decision to the knowledge base.
    
    Args:
        knowledge_base: Knowledge base dictionary
        decision: The decision made
        rationale: Why this decision was made
        category: Decision category
        scope: "project", "conversation", or "permanent"
        confidence: "low", "medium", or "high"
        
    Returns:
        Updated knowledge base
    """
    now = datetime.utcnow().isoformat() + 'Z'
    
    # Generate simple ID
    d_count = len(knowledge_base["decisions"]) + 1
    d_id = f"d{d_count:03d}"
    
    decision_entry = {
        "id": d_id,
        "decision": decision,
        "rationale": rationale,
        "date": now,
        "category": category,
        "scope": scope,
        "confidence": confidence,
        "supersedes": None,
        "related_questions": [],
        "impact": "",
        "status": "active",
        "tags": []
    }
    
    knowledge_base["decisions"].append(decision_entry)
    knowledge_base["statistics"]["total_decisions"] += 1
    knowledge_base["last_updated"] = now
    
    return knowledge_base


def add_snapshot(knowledge_base: Dict, snapshot_type: str,
                message_count: int, tool_call_count: int,
                active_task: str, key_context: str) -> Dict:
    """
    Add a context snapshot to the knowledge base.
    
    Args:
        knowledge_base: Knowledge base dictionary
        snapshot_type: "periodic", "pre_handover", or "milestone"
        message_count: Current message count
        tool_call_count: Current tool call count
        active_task: Description of current task
        key_context: Essential context string
        
    Returns:
        Updated knowledge base
    """
    now = datetime.utcnow().isoformat() + 'Z'
    
    # Generate simple ID
    s_count = len(knowledge_base["context_snapshots"]) + 1
    s_id = f"s{s_count:03d}"
    
    memory_score = calculate_memory_score(message_count, tool_call_count)
    
    snapshot_entry = {
        "id": s_id,
        "date": now,
        "snapshot_type": snapshot_type,
        "message_count": message_count,
        "tool_call_count": tool_call_count,
        "memory_score": memory_score,
        "active_task": active_task,
        "task_status": "in_progress",
        "completion_percentage": 0,
        "filesystem_state": [],
        "workspace_state": [],
        "key_context": key_context,
        "open_questions": [],
        "next_steps": [],
        "blockers": [],
        "tags": []
    }
    
    knowledge_base["context_snapshots"].append(snapshot_entry)
    knowledge_base["statistics"]["total_snapshots"] += 1
    knowledge_base["last_updated"] = now
    
    return knowledge_base


def create_handover_frontmatter(message_count: int, tool_call_count: int,
                                 project: str, author: str = "Colin Bitterfield",
                                 email: str = "colin@bitterfield.com") -> Dict:
    """
    Create YAML frontmatter for handover document.
    
    Args:
        message_count: Number of messages
        tool_call_count: Number of tool calls
        project: Project name
        author: Author name
        email: Author email
        
    Returns:
        Dictionary with frontmatter data
    """
    now = datetime.utcnow()
    memory_score = calculate_memory_score(message_count, tool_call_count)
    
    frontmatter = {
        "handover_date": now.isoformat() + 'Z',
        "conversation_duration": None,  # To be filled manually
        "message_count": message_count,
        "tool_call_count": tool_call_count,
        "memory_score": memory_score,
        "version": "1.0.0",
        "author": author,
        "email": email,
        "project": project,
        "previous_handover": None,
        "next_conversation_priority": "high"
    }
    
    return frontmatter


def main():
    """Main function for CLI usage."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Conversation Continuity Helper Utilities"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Memory score command
    score_parser = subparsers.add_parser("score", help="Calculate memory score")
    score_parser.add_argument("messages", type=int, help="Message count")
    score_parser.add_argument("tool_calls", type=int, help="Tool call count")
    
    # Initialize knowledge base command
    init_parser = subparsers.add_parser("init", help="Initialize knowledge base")
    init_parser.add_argument("project_path", help="Project root path")
    init_parser.add_argument("--output", "-o", default="conversation-knowledge.yaml",
                           help="Output filename")
    init_parser.add_argument("--versioning", choices=["internal", "filename"],
                           default="internal", help="Versioning preference")
    
    # Validate knowledge base command
    val_parser = subparsers.add_parser("validate", help="Validate knowledge base")
    val_parser.add_argument("filepath", help="Path to knowledge base file")
    
    args = parser.parse_args()
    
    if args.command == "score":
        score = calculate_memory_score(args.messages, args.tool_calls)
        status = get_memory_status(score)
        print(f"Memory Score: {score}")
        print(f"Status: {status['status']} ({status['level']})")
        print(f"Recommendation: {status['recommendation']}")
        
    elif args.command == "init":
        kb = init_knowledge_base(args.project_path, args.versioning)
        if save_knowledge_base(kb, args.output):
            print(f"Knowledge base initialized: {args.output}")
        else:
            print("Failed to create knowledge base", file=sys.stderr)
            sys.exit(1)
            
    elif args.command == "validate":
        kb = load_knowledge_base(args.filepath)
        if kb is None:
            sys.exit(1)
        
        errors = validate_knowledge_base(kb)
        if errors:
            print("Validation errors:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
        else:
            print("Knowledge base is valid")
            
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
