import sqlite3

messages = [
    {
        "id": 1,
        "sender": "nicolehaynes@yang.com",
        "subject": "Urgent: Last Chance to Confirm Your Seminar Attendance",
        "message": "We've noticed you haven't confirmed your attendance for the upcoming music industry seminar. This is your last chance to secure your spot among other leading professionals. Don't miss out on this opportunity to enhance your network and knowledge.",
        "timestamp": "2024-03-24 16:31:43",
        "urgent": True
    },
    {
        "id": 2,
        "sender": "acannon@miller-adams.com",
        "subject": "Decade Review: Industry Insights and Future Trends",
        "message": "As we enter a new decade, it's crucial to look back at our achievements and set a clear path forward. This newsletter highlights the major milestones of the past ten years and outlines what's next for our company. Your feedback and insights are valuable as we shape our future strategies.",
        "timestamp": "2024-02-29 16:31:43",
        "urgent": False
    },
    {
        "id": 3,
        "sender": "jenniferbates@hotmail.com",
        "subject": "Meeting Reminder: Strategy Session This Wednesday",
        "message": "A gentle reminder about our strategy session scheduled for this Wednesday. We'll discuss our progress, upcoming elections, and growth opportunities. Your participation and insights are highly valued as we navigate these topics. Please prepare any materials or questions you have in advance.",
        "timestamp": "2024-03-02 16:31:43",
        "urgent": True
    },
    {
        "id": 4,
        "sender": "pclark@yahoo.com",
        "subject": "Exclusive Event: Customer Appreciation Night",
        "message": "We're thrilled to invite you to our exclusive Customer Appreciation Night. This event is a token of our gratitude for your continued support and loyalty. Join us for an evening of entertainment, networking, and special surprises. Your presence would mean the world to us.",
        "timestamp": "2024-02-24 16:31:43",
        "urgent": False
    },
    {
        "id": 5,
        "sender": "roachbill@johnson.com",
        "subject": "Kitchen Remodel Material Selection Meeting",
        "message": "We're scheduled to meet and discuss the materials for your upcoming kitchen remodel. This session will cover everything from countertops to cabinets, ensuring we align with your vision and budget. Please confirm your availability for this critical step in bringing your dream kitchen to life.",
        "timestamp": "2024-03-23 16:31:43",
        "urgent": True
    },
    {
        "id": 6,
        "sender": "sharon20@jimenez.info",
        "subject": "Volunteer Event: Local Park Cleanup Initiative",
        "message": "Join us for a day of community service at our local park this weekend. Your efforts will help maintain the beauty and health of our shared green spaces. This is a fantastic opportunity to enjoy the outdoors, meet your neighbors, and make a positive impact. We hope to see you there!",
        "timestamp": "2024-03-16 16:31:43",
        "urgent": False
    },
    {
        "id": 7,
        "sender": "jacksonpatricia@braun-bradshaw.biz",
        "subject": "New Art Exhibit Opening: 'Images of the Evening'",
        "message": "We're excited to announce the opening of our new art exhibit, 'Images of the Evening,' featuring contemporary works that explore the essence of nighttime. Join us for the opening night reception to enjoy the artwork, meet the artists, and engage with the local art community.",
        "timestamp": "2024-03-22 16:31:43",
        "urgent": False
    },
    {
        "id": 8,
        "sender": "qrobertson@schultz.com",
        "subject": "Business Travel Itinerary for Upcoming Trip",
        "message": "Please find attached the itinerary for your upcoming business trip, including flight details, hotel reservations, and scheduled meetings. We've also included recommendations for dining and leisure to enhance your stay. Your feedback post-trip would be greatly appreciated.",
        "timestamp": "2024-03-05 16:31:43",
        "urgent": False
    },
    {
        "id": 9,
        "sender": "lmontgomery@clark.net",
        "subject": "School Fundraiser: Support our Local Students",
        "message": "Our annual school fundraiser is just around the corner, aiming to support our students with new educational resources and extracurricular activities. This year, we're focusing on improving our technology tools and sports equipment. Every donation, big or small, makes a significant difference. Let's come together to invest in our children's future.",
        "timestamp": "2024-03-01 16:31:43",
        "urgent": False
        },
        {
        "id": 10,
        "sender": "james78@hotmail.com",
        "subject": "Webinar Reminder: Expert Strategies for Business Growth",
        "message": "Don't forget to join us for tomorrow's webinar, featuring industry experts sharing their top strategies for business growth in the current economic climate. This is a unique opportunity to gain insights and ask questions that could benefit your business. Secure your spot now if you haven't already.",
        "timestamp": "2024-02-28 16:31:43",
        "urgent": False
        },
        {
        "id": 11,
        "sender": "acooper@gmail.com",
        "subject": "Community Meeting: Addressing Local Concerns",
        "message": "Your presence is requested at the upcoming community meeting, where we'll discuss pressing issues affecting our neighborhood, including safety, development, and local politics. This is your chance to voice your concerns and contribute to shaping the future of our community.",
        "timestamp": "2024-03-13 16:31:43",
        "urgent": False
        },
        {
        "id": 12,
        "sender": "ochen@yahoo.com",
        "subject": "Thank You: A Message of Appreciation from Our Team",
        "message": "We want to extend our heartfelt thanks for your continuous support and contribution to our mission. Your efforts have been instrumental in our success, and we're truly grateful. Let's continue to make a positive impact together.",
        "timestamp": "2024-02-28 16:31:43",
        "urgent": False
        },
        {
        "id": 13,
        "sender": "jamiesnyder@ferguson.com",
        "subject": "Weekly Brief: Important Updates and Announcements",
        "message": "This week's brief includes crucial updates on our projects, upcoming deadlines, and new team members. We also have a section on health and safety reminders. Please take a moment to review these announcements to stay informed and prepared.",
        "timestamp": "2024-03-09 16:31:43",
        "urgent": False
        },
        {
        "id": 14,
        "sender": "ryanyang@yahoo.com",
        "subject": "Investment Opportunity: Exploring New Markets",
        "message": "We're excited to share a unique investment opportunity that has emerged in the Eastern markets. This brief outlines the potential benefits and risks, aiming to provide you with comprehensive insights to make an informed decision. Your feedback would be invaluable as we consider this venture.",
        "timestamp": "2024-03-11 16:31:43",
        "urgent": False
        },
        {
        "id": 15,
        "sender": "smithjoanna@hotmail.com",
        "subject": "Urgent: Confirm Your Attendance for the Performance Review Meeting",
        "message": "Please confirm your attendance for the upcoming performance review meeting. It's crucial that all team members are present as we discuss achievements, areas for improvement, and set goals for the next quarter. Your participation is key to our collective success.",
        "timestamp": "2024-02-28 16:31:43",
        "urgent": True
        },
        {
        "id": 16,
        "sender": "xkirk@hotmail.com",
        "subject": "Spring Gardening Workshop: Enhance Your Green Space",
        "message": "Spring is around the corner, and we're hosting a gardening workshop to help you prepare your outdoor spaces. From selecting the right plants to sustainable gardening practices, join us to learn and share tips for a beautiful and eco-friendly garden. RSVP today to secure your spot.",
        "timestamp": "2024-03-02 16:31:43",
        "urgent": False
        },
        {
        "id": 17,
        "sender": "justinwaters@kelly-mendez.com",
        "subject": "Leadership Conference: Navigating Challenges in the Digital Age",
        "message": "We're pleased to invite you to the upcoming Leadership Conference, where we'll explore the challenges and opportunities of leading in the digital age. This event will feature keynote speakers, interactive sessions, and networking opportunities. Your attendance would add great value.",
        "timestamp": "2024-03-04 16:31:43",
        "urgent": False
        },
            {
        "id": 18,
        "sender": "wisemelody@bailey.com",
        "subject": "Urgent: Support Needed for Local Shelter",
        "message": "Our local shelter is facing unprecedented challenges and urgently needs support. We're reaching out to our community for donations of goods, volunteer time, or financial contributions. Every bit helps in making a difference for those in need. Let's show our community spirit and help where we can.",
        "timestamp": "2024-03-08 16:31:43",
        "urgent": True
    },
    {
        "id": 19,
        "sender": "kellymartin@williams-west.com",
        "subject": "Furniture Design Workshop: Crafting Comfortable Spaces",
        "message": "Join us for an exclusive workshop on designing and crafting comfortable, beautiful living spaces with our latest furniture collection. Learn from our top designers, get hands-on experience, and inspire your home decor. Spaces are limited, so reserve your spot now!",
        "timestamp": "2024-03-23 16:31:43",
        "urgent": False
    },
    {
        "id": 20,
        "sender": "tanya75@gmail.com",
        "subject": "Discussion Panel: The Future of Work",
        "message": "We're hosting a panel discussion on the Future of Work, featuring insights from industry leaders on evolving workplace trends, remote work, and employee wellbeing. Join us for a thought-provoking session and a chance to network with professionals from various fields. Register today to secure your participation.",
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


def reset():
    connection = sqlite3.connect('messages.db')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS messages')
    connection.commit()
    connection.close()