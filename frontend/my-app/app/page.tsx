"use client";

import { useState } from "react";

export default function Home() {
  const [formData, setFormData] = useState({
    study_hours_per_day: 6,
    sleep_hours: 6,
    screen_time_hours: 6,
    breaks_per_day: 3,
    stress_level: 5,
    physical_activity: 30,
    consistency_score: 6,
  });

  const [result, setResult] = useState<any>(null);
  const [advice, setAdvice] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  const handleChange = (e: any) => {
    setFormData({ ...formData, [e.target.name]: Number(e.target.value) });
  };

  const generateAdvice = (res: any) => {
    const tips: string[] = [];

    if (res.productivity_score < 50) {
      tips.push("📉 You are overloaded. Try focused 25–30 minute study sessions.");
    } else if (res.productivity_score < 75) {
      tips.push("📈 You are doing okay. Improving consistency can help a lot.");
    } else {
      tips.push("🚀 You are in a strong productivity zone. Maintain this rhythm.");
    }

    if (res.burnout_risk === "Yes") {
      tips.push("⚠️ Burnout risk detected. Reduce workload and prioritize rest.");
    } else {
      tips.push("✅ Burnout risk is low. Your balance looks healthy.");
    }

    if (formData.sleep_hours < 6) {
      tips.push("😴 Try to increase sleep to 7–8 hours for recovery.");
    }

    if (formData.stress_level > 7) {
      tips.push("🧘 High stress detected. Consider breathing or light movement.");
    }

    return tips;
  };

  const predict = async () => {
    setLoading(true);

    const response = await fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });

    const data = await response.json();
    setResult(data);
    setAdvice(generateAdvice(data));
    setLoading(false);
  };

  const labels: any = {
    study_hours_per_day: "📚 Study Hours",
    sleep_hours: "😴 Sleep",
    screen_time_hours: "📱 Screen Time",
    breaks_per_day: "☕ Breaks",
    stress_level: "😣 Stress",
    physical_activity: "🏃 Activity",
    consistency_score: "📅 Consistency",
  };

  return (
    <main
      style={{
        minHeight: "100vh",
        backgroundImage:
          "url('https://images.unsplash.com/photo-1513258496099-48168024aec0')",
        backgroundSize: "cover",
        backgroundPosition: "center",
        position: "relative",
      }}
    >
      {/* Overlay */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "linear-gradient(to right, rgba(2,6,23,0.85), rgba(30,64,175,0.55))",
        }}
      />

      {/* Content */}
      <div
        style={{
          position: "relative",
          minHeight: "100vh",
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "40px",
          padding: "40px",
          color: "white",
        }}
      >
        {/* LEFT: STORY */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
          }}
        >
          <h1 style={{ fontSize: "42px", lineHeight: 1.2 }}>
            Studying shouldn’t
            <br />
            feel like burnout.
          </h1>

          <p style={{ marginTop: "20px", fontSize: "18px", color: "#e5e7eb" }}>
            Many students struggle silently with stress, fatigue, and pressure.
            <br />
            This AI system helps you understand your state and improve it —
            before burnout hits.
          </p>

        </div>

        {/* RIGHT: AI CARD */}
        <div
          style={{
            background: "rgba(255,255,255,0.18)",
            backdropFilter: "blur(16px)",
            borderRadius: "20px",
            padding: "28px",
            border: "1px solid rgba(255,255,255,0.3)",
            boxShadow: "0 30px 60px rgba(0,0,0,0.5)",
          }}
        >
          <h2 style={{ textAlign: "center", marginBottom: "20px" }}>
            🤖 AI Productivity Advisor
          </h2>

          {Object.keys(formData).map((key) => (
            <div key={key} style={{ marginBottom: "14px" }}>
              <label style={{ fontWeight: 600 }}>{labels[key]}</label>
              <input
                type="range"
                min="0"
                max="10"
                name={key}
                value={formData[key as keyof typeof formData]}
                onChange={handleChange}
                style={{ width: "100%" }}
              />
              <div style={{ textAlign: "right", fontSize: "13px" }}>
                {formData[key as keyof typeof formData]}
              </div>
            </div>
          ))}

          <button
            onClick={predict}
            disabled={loading}
            style={{
              width: "100%",
              padding: "12px",
              background:
                "linear-gradient(135deg, #22d3ee, #6366f1)",
              color: "#020617",
              border: "none",
              borderRadius: "12px",
              fontSize: "16px",
              fontWeight: 700,
              cursor: "pointer",
              marginTop: "10px",
            }}
          >
            {loading ? "Analyzing..." : "Predict My Insights"}
          </button>

          {result && (
            <div style={{ marginTop: "20px" }}>
              <h3>📊 Your Results</h3>
              <p>
                Productivity:{" "}
                <strong style={{ color: "#0b66f9" }}>
                  {result.productivity_score}
                </strong>
              </p>
              <p>
                Burnout Risk:{" "}
                <strong
                  style={{
                    color:
                      result.burnout_risk === "Yes"
                        ? "#f87171"
                        : "#4ade80",
                  }}
                >
                  {result.burnout_risk}
                </strong>
              </p>
            </div>
          )}

          {advice.length > 0 && (
            <div
              style={{
                marginTop: "18px",
                background: "rgba(255,255,255,0.15)",
                padding: "14px",
                borderRadius: "12px",
              }}
            >
              <h3>🧠 Personalized Advice</h3>
              <ul>
                {advice.map((tip, i) => (
                  <li key={i} style={{ marginBottom: "6px" }}>
                    {tip}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
