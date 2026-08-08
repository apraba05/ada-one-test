"use client";

import { useState } from "react";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

type Source = { title: string; url: string; score: number };
type AskResponse = {
  answer: string;
  refused: boolean;
  sources: Source[];
  retrieval_score: number;
  judge_score: number | null;
  judge_reasoning: string;
  thresholds: { retrieval: number; judge: number };
};

const EXAMPLES = [
  "Can I connect my Zendesk help center?",
  "How do I create a knowledge article in Ada?",
  "What are best practices for setting up knowledge?",
];

// Long right-arrow inside the signature charcoal circle (ADA-CX.md §5.1).
function ArrowRight() {
  return (
    <svg viewBox="0 0 14 12" fill="none" className="h-3 w-3.5" aria-hidden="true">
      <path d="M8 1l5 5-5 5M13 6H1" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

// Render inline [Title] citations as subtle green chips and **bold** as medium
// weight; everything else plain. (The local model emits light markdown.)
function AnswerText({ text }: { text: string }) {
  const parts = text.split(/(\[[^\]]+\]|\*\*[^*]+\*\*)/g);
  return (
    <p className="whitespace-pre-wrap text-[17px] leading-[1.55] text-charcoal">
      {parts.map((p, i) => {
        if (/^\[[^\]]+\]$/.test(p)) {
          return (
            <span key={i} className="mx-0.5 rounded-md bg-green-100 px-1.5 py-0.5 text-[13px] font-medium text-green align-baseline">
              {p.slice(1, -1)}
            </span>
          );
        }
        if (/^\*\*[^*]+\*\*$/.test(p)) {
          return (
            <span key={i} className="font-medium text-charcoal">
              {p.slice(2, -2)}
            </span>
          );
        }
        return <span key={i}>{p}</span>;
      })}
    </p>
  );
}

function Meter({ label, value, threshold }: { label: string; value: number | null; threshold: number }) {
  const pass = value !== null && value >= threshold;
  const pct = value === null ? 0 : Math.min(100, Math.round(value * 100));
  return (
    <div>
      <div className="mb-1 flex items-baseline justify-between text-[13px]">
        <span className="text-pewter">{label}</span>
        <span className="font-medium tabular-nums text-charcoal">
          {value === null ? "—" : value.toFixed(2)}
          <span className="text-pewter"> / ≥ {threshold}</span>
          <span className={pass ? "ml-2 text-green" : "ml-2 text-pewter"}>{value === null ? "" : pass ? "✓ pass" : "✗ fail"}</span>
        </span>
      </div>
      <div className="h-1.5 w-full overflow-hidden rounded-full bg-grey">
        <div className={`h-full rounded-full ${pass ? "bg-green" : "bg-pewter"}`} style={{ width: `${pct}%` }} />
      </div>
    </div>
  );
}

export default function Home() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AskResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function ask(q: string) {
    const query = q.trim();
    if (!query || loading) return;
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await fetch(`${API_URL}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: query }),
      });
      if (!res.ok) {
        const detail = await res.json().catch(() => null);
        throw new Error(detail?.detail ?? `Request failed (${res.status})`);
      }
      setResult((await res.json()) as AskResponse);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Something went wrong reaching the answering service.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen">
      {/* Nav — floating white pill (ADA-CX.md §Hero/Nav) */}
      <div className="mx-auto max-w-3xl px-4 pt-4">
        <nav className="flex items-center justify-between rounded-full bg-white-fr px-5 py-3 shadow-[0_1px_3px_rgba(10,11,12,0.08)]">
          <div className="flex items-center gap-2">
            <span className="text-[20px] font-medium tracking-tight text-charcoal">Ada</span>
            <span className="text-[15px] text-pewter">Knowledge QA</span>
          </div>
          <span className="text-[12px] uppercase tracking-wide text-pewter">Internal eval tool</span>
        </nav>
      </div>

      <main className="mx-auto max-w-3xl px-4 pb-24 pt-14">
        <h1 className="max-w-2xl text-[44px] leading-[1.02] tracking-tight text-charcoal">
          Knowledge base answers you can trust
        </h1>
        <p className="mt-4 max-w-xl text-[18px] leading-[1.5] text-charcoal/70">
          Ask about setting up your Ada AI agent&rsquo;s knowledge base. Answers are grounded in Ada&rsquo;s
          own documentation — and the tool refuses, rather than guesses, when it isn&rsquo;t confident.
        </p>

        {/* Input card */}
        <form
          onSubmit={(e) => {
            e.preventDefault();
            ask(question);
          }}
          className="mt-8 rounded-2xl bg-white-fr p-3 shadow-[0_1px_3px_rgba(10,11,12,0.08)]"
        >
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                ask(question);
              }
            }}
            rows={2}
            placeholder="e.g. Can I connect my Zendesk help center?"
            className="w-full resize-none rounded-xl bg-transparent px-3 py-2 text-[17px] text-charcoal placeholder:text-pewter focus:outline-none"
          />
          <div className="flex items-center justify-between px-1 pt-1">
            <span className="text-[13px] text-pewter">Press Enter to ask</span>
            <button
              type="submit"
              disabled={loading || !question.trim()}
              className="group flex items-center gap-2 rounded-full bg-blue py-2 pl-5 pr-2 text-[16px] text-charcoal transition-opacity disabled:opacity-40"
            >
              {loading ? "Searching…" : "Ask"}
              <span className="flex size-9 items-center justify-center rounded-full bg-charcoal text-white-fr">
                <ArrowRight />
              </span>
            </button>
          </div>
        </form>

        {/* Example chips */}
        {!result && !loading && !error && (
          <div className="mt-5 flex flex-wrap gap-2">
            {EXAMPLES.map((ex) => (
              <button
                key={ex}
                onClick={() => {
                  setQuestion(ex);
                  ask(ex);
                }}
                className="rounded-full border border-grey bg-white-fr px-4 py-2 text-[14px] text-charcoal/80 transition-colors hover:bg-off-white"
              >
                {ex}
              </button>
            ))}
          </div>
        )}

        {/* Loading state */}
        {loading && (
          <div className="mt-8 animate-pulse rounded-2xl border-l-[6px] border-grey bg-white-fr p-6 shadow-[0_1px_3px_rgba(10,11,12,0.06)]">
            <div className="mb-3 h-3 w-40 rounded-full bg-grey" />
            <div className="mb-2 h-3 w-full rounded-full bg-grey" />
            <div className="mb-2 h-3 w-11/12 rounded-full bg-grey" />
            <div className="h-3 w-3/4 rounded-full bg-grey" />
            <p className="mt-4 text-[14px] text-pewter">Searching the knowledge base and checking confidence…</p>
          </div>
        )}

        {/* Error state */}
        {error && (
          <div className="mt-8 rounded-2xl border-l-[6px] border-gold bg-white-fr p-6 shadow-[0_1px_3px_rgba(10,11,12,0.06)]">
            <p className="text-[15px] font-medium text-charcoal">Couldn&rsquo;t reach the answering service</p>
            <p className="mt-1 text-[14px] text-charcoal/70">{error}</p>
          </div>
        )}

        {/* Result */}
        {result && !loading && (
          <div className="mt-8">
            {result.refused ? (
              // Refusal — deliberately distinct: graphite, no green (ADA-CX.md-derived).
              <div className="rounded-2xl rounded-l-2xl border-l-[6px] border-graphite bg-off-white p-6 shadow-[0_1px_3px_rgba(10,11,12,0.06)]">
                <div className="mb-2 flex items-center gap-2">
                  <span className="flex size-6 items-center justify-center rounded-full bg-graphite text-[13px] text-white-fr">i</span>
                  <span className="text-[13px] font-medium uppercase tracking-wide text-graphite">Not enough information</span>
                </div>
                <p className="text-[17px] leading-[1.55] text-charcoal">{result.answer}</p>
              </div>
            ) : (
              // Answer — confident: white card, green left border.
              <div className="rounded-2xl rounded-l-2xl border-l-[6px] border-green bg-white-fr p-6 shadow-[0_1px_3px_rgba(10,11,12,0.08)]">
                <div className="mb-3 flex items-center gap-2">
                  <span className="flex size-6 items-center justify-center rounded-full bg-green text-[13px] text-white-fr">✓</span>
                  <span className="text-[13px] font-medium uppercase tracking-wide text-green">Grounded answer</span>
                </div>
                <AnswerText text={result.answer} />

                {result.sources.length > 0 && (
                  <div className="mt-5 border-t border-grey pt-4">
                    <p className="mb-2 text-[13px] text-pewter">Sources</p>
                    <div className="flex flex-wrap gap-2">
                      {result.sources.map((s) => (
                        <a
                          key={s.url}
                          href={s.url}
                          target="_blank"
                          rel="noreferrer"
                          className="group flex items-center gap-1.5 rounded-full bg-blue-100 px-3 py-1.5 text-[13px] text-charcoal transition-colors hover:bg-blue"
                        >
                          {s.title}
                          <span className="text-charcoal/60 transition-transform group-hover:translate-x-0.5">↗</span>
                        </a>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* Confidence trace — collapsible, secondary (ADA-CX.md-derived) */}
            <details className="group mt-3 rounded-2xl bg-white-fr p-4 shadow-[0_1px_3px_rgba(10,11,12,0.06)]">
              <summary className="flex cursor-pointer list-none items-center justify-between text-[14px] text-charcoal/80">
                <span className="flex items-center gap-2">
                  <span className="text-pewter transition-transform group-open:rotate-90">▸</span>
                  Confidence trace
                </span>
                <span className="tabular-nums text-[13px] text-pewter">
                  retrieval {result.retrieval_score.toFixed(2)} · judge{" "}
                  {result.judge_score === null ? "—" : result.judge_score.toFixed(2)}
                </span>
              </summary>
              <div className="mt-4 space-y-4">
                <Meter label="Retrieval similarity (max cosine)" value={result.retrieval_score} threshold={result.thresholds.retrieval} />
                <Meter label="LLM judge groundedness" value={result.judge_score} threshold={result.thresholds.judge} />
                <div className="rounded-xl bg-off-white p-3">
                  <p className="mb-1 text-[12px] uppercase tracking-wide text-pewter">Judge reasoning</p>
                  <p className="text-[14px] leading-[1.5] text-charcoal/80">{result.judge_reasoning}</p>
                </div>
                <p className="text-[12px] text-pewter">
                  Both checks must pass to answer. If either falls below its threshold, the tool refuses rather than guess.
                </p>
              </div>
            </details>
          </div>
        )}
      </main>
    </div>
  );
}
