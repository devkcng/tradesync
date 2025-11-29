def generate_trade_review_prompt(trade_data):
    return f"""
    You are an expert trading coach. Analyze this trade:
    
    Pair: {trade_data['pair']}
    Direction: {trade_data['direction']}
    Outcome: ${trade_data['pnl']}
    User Emotion: {trade_data['emotion']}
    User Notes: "{trade_data['notes']}"
    
    1. Did the user follow logical risk management?
    2. Does the emotion tag ("{trade_data['emotion']}") correlate with the loss/win?
    3. Give 1 actionable tip for the next trade.
    """
