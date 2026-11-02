with open('ClockworkPathfinder/testing/combat_sim/generate_all_templates.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('"ClockworkRifleman": {')
end = text.find('"Merchant": {', start)
print(text[start:end])
