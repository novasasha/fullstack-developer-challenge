import sqlite3

messages = [
    {
        "id": 1,
        "sender": "nicolehaynes@yang.com",
        "subject": "Way able role your reach.",
        "message": "Poor explain recent music agreement rich. Other and weight start its authority those claim.",
        "timestamp": "2024-03-24 16:31:43",
        "urgent": True
    },
    {
        "id": 2,
        "sender": "acannon@miller-adams.com",
        "subject": "Center take foreign and decade other senior.",
        "message": "Buy adult reduce add. More strong billion possible walk.",
        "timestamp": "2024-02-29 16:31:43",
        "urgent": False
    },
    {
        "id": 3,
        "sender": "jenniferbates@hotmail.com",
        "subject": "Meeting them factor prepare easy pass.",
        "message": "Trial evidence customer owner kid fill particularly. Clear decade this election every growth. Up usually suddenly population enjoy. Late everyone section southern.",
        "timestamp": "2024-03-02 16:31:43",
        "urgent": False
    },
    {
        "id": 4,
        "sender": "pclark@yahoo.com",
        "subject": "Which population best customer room.",
        "message": "Audience yes of attention. War like see.",
        "timestamp": "2024-02-24 16:31:43",
        "urgent": False
    },
    {
        "id": 5,
        "sender": "roachbill@johnson.com",
        "subject": "Respond most kitchen material.",
        "message": "Since box material rate. Suffer rather necessary. Lawyer discover near plant pretty produce situation.",
        "timestamp": "2024-03-23 16:31:43",
        "urgent": True
    },
    {
        "id": 6,
        "sender": "sharon20@jimenez.info",
        "subject": "Study plant enjoy voice end entire line public.",
        "message": "Recognize either six worker. Often edge many maybe young son.",
        "timestamp": "2024-03-16 16:31:43",
        "urgent": False
    },
    {
        "id": 7,
        "sender": "jacksonpatricia@braun-bradshaw.biz",
        "subject": "Because picture seek sense evening inside image.",
        "message": "Industry hour instead establish option opportunity plant. House main respond easy product community rich. Finally physical office theory as learn computer.",
        "timestamp": "2024-03-22 16:31:43",
        "urgent": False
    },
    {
        "id": 8,
        "sender": "qrobertson@schultz.com",
        "subject": "Travel begin business PM father then.",
        "message": "Experience exactly nature high. Letter final scene deal choice.",
        "timestamp": "2024-03-05 16:31:43",
        "urgent": False
    },
    {
        "id": 9,
        "sender": "lmontgomery@clark.net",
        "subject": "Bring official pick seven.",
        "message": "Anything whatever agency. Parent control town student short now team reach. Themselves floor whole simply.",
        "timestamp": "2024-03-01 16:31:43",
        "urgent": False
    },
    {
        "id": 10,
        "sender": "james78@hotmail.com",
        "subject": "Through example subject between while expert point.",
        "message": "Wife hundred she let up group however. Significant draw natural road week single season.",
        "timestamp": "2024-02-28 16:31:43",
        "urgent": False
    },
    {
        "id": 11,
        "sender": "acooper@gmail.com",
        "subject": "Often against concern.",
        "message": "Surface attention different federal personal your situation. Amount north purpose politics interview after reason.",
        "timestamp": "2024-03-13 16:31:43",
        "urgent": False
    },
    {
        "id": 12,
        "sender": "ochen@yahoo.com",
        "subject": "Every city our avoid thank the help.",
        "message": "Lot sort best couple policy report phone. Out office society city development.",
        "timestamp": "2024-02-28 16:31:43",
        "urgent": False
    },
    {
        "id": 13,
        "sender": "jamiesnyder@ferguson.com",
        "subject": "Street enough not question work term.",
        "message": "Attention lot week present actually. Television fire something hair night school. Recent among increase lose away little stop.",
        "timestamp": "2024-03-09 16:31:43",
        "urgent": False
    },
    {
        "id": 14,
        "sender": "ryanyang@yahoo.com",
        "subject": "Stock chance make land east.",
        "message": "Much Mr yeah also story nothing. Hair American skill lose fight itself. Treatment ask major figure.",
        "timestamp": "2024-03-11 16:31:43",
        "urgent": False
    },
    {
        "id": 15,
        "sender": "smithjoanna@hotmail.com",
        "subject": "Woman away PM performance almost trip minute direction.",
        "message": "Write away thousand only serve.",
        "timestamp": "2024-02-28 16:31:43",
        "urgent": True
    },
    {
        "id": 16,
        "sender": "xkirk@hotmail.com",
        "subject": "Able mother particular important spring executive yard.",
        "message": "Seven word your prepare. Material plan similar amount for edge will. As say eight let member.",
        "timestamp": "2024-03-02 16:31:43",
        "urgent": False
    },
    {
        "id": 17,
        "sender": "justinwaters@kelly-mendez.com",
        "subject": "She measure its born.",
        "message": "Majority responsibility prove brother. Ask others research woman conference describe. Build very peace hour.",
        "timestamp": "2024-03-04 16:31:43",
        "urgent": False
    },
    {
        "id": 18,
        "sender": "wisemelody@bailey.com",
        "subject": "Agency deal support theory.",
        "message": "Short stuff response physical risk. Position later manage seven often sure.",
        "timestamp": "2024-03-08 16:31:43",
        "urgent": True
    },
    {
        "id": 19,
        "sender": "kellymartin@williams-west.com",
        "subject": "Hundred fast specific chair pretty prepare.",
        "message": "Seat produce involve whose occur bit. Whom safe few yes.",
        "timestamp": "2024-03-23 16:31:43",
        "urgent": False
    },
    {
        "id": 20,
        "sender": "tanya75@gmail.com",
        "subject": "As example involve.",
        "message": "Today each red discussion True. Inside level two stay hour avoid.",
        "timestamp": "2024-02-27 16:31:43",
        "urgent": False
    }
]

def init():
    connection = sqlite3.connect('messages.db')
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages
            (id INTEGER PRIMARY KEY, sender TEXT, subject TEXT, message TEXT, timestamp TEXT, urgent BOOLEAN)
    """)

    # Only re-populate the table if it's empty
    cursor.execute('SELECT COUNT(*) FROM messages')
    if cursor.fetchone()[0] == 0:
        query = 'INSERT INTO messages (sender, subject, message, timestamp, urgent) VALUES (:sender, :subject, :message, :timestamp, :urgent)'
        cursor.executemany(query, messages)

    connection.commit()
    connection.close()
