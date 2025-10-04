"use client";
import { useState, FormEvent } from "react";
import "./globals.css"; // CSS file

// Example quotes from Gita
const quotes = [
  "Karmanye vadhikaraste, Ma phaleshu kadachana",
  "Yada yada hi dharmasya, glanir bhavati bharata",
  "Abhyasena tu kaunteya, vairagyena cha grhyate",
  "Yoga karmasu kaushalam"
];

export default function Home() {
  const [quote, setQuote] = useState<string>("");
  const [story, setStory] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!quote) return;

    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:5000/story", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ quote }),
      });
      const data: { story: string } = await res.json();
      setStory(data.story);
    } catch (err) {
      console.error(err);
      setStory("⚠️ Error generating story");
    }
    setLoading(false);
  };

  return (
    <div>
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-content">
          <h1>📖 Bhagwat Gita Storyteller</h1>
          <p>Enter any shloka or quote and get a relatable story for modern life!</p>
          <form onSubmit={handleSubmit} className="hero-form">
            <input
              type="text"
              placeholder="Enter a shloka or quote"
              value={quote}
              onChange={(e) => setQuote(e.target.value)}
            />
            <button type="submit">{loading ? "Generating..." : "Get Story"}</button>
          </form>
          {story && (
            <div className="story-box">
              <h3>Story:</h3>
              <p>{story}</p>
            </div>
          )}
        </div>
        <div className="hero-image">
          <img src="/gita_hero.jpg" alt="Bhagwat Gita" />
        </div>
      </section>

      {/* About Section */}
      <section className="about">
        <h2>About This Website</h2>
        <p>
          This website uses AI to bring Bhagwat Gita shlokas to life. Enter a shloka and
          get a modern, relatable story that helps you understand its meaning in today's context.
        </p>
      </section>

      {/* Quotes Section */}
      <section className="quotes">
        <h2>Inspiring Quotes</h2>
        <div className="quote-list">
          {quotes.map((q, idx) => (
            <div key={idx} className="quote-card">
              <p>"{q}"</p>
            </div>
          ))}
        </div>
      </section>

      {/* Contact Section */}
      <section className="contact">
        <h2>Contact</h2>
        <p>Have suggestions or feedback? Reach out to us!</p>
        <form className="contact-form">
          <input type="text" placeholder="Your Name" />
          <input type="email" placeholder="Your Email" />
          <textarea placeholder="Your Message" rows={4}></textarea>
          <button type="submit">Send Message</button>
        </form>
      </section>

      {/* Footer */}
      <footer>
        <p>© 2025 Bhagwat Gita Storyteller. All rights reserved.</p>
      </footer>
    </div>
  );
}
