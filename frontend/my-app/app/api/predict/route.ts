import { NextResponse } from "next/server";

export async function POST(req: Request) {
  const body = await req.json();

  const response = await fetch(
    "https://ai-study-productivity-and-burnout-risk.onrender.com/predict",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    }
  );

  const data = await response.json();

  return NextResponse.json({
  productivity_score: data.Productivity_Score,
  burnout_risk: data.Burnout_Risk,
});

}
