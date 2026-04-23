-- Supabase Schema Migration Notes
-- =================================
-- Required tables for Aescode website functionality.
-- Run these in the Supabase SQL editor.

-- 1. Newsletter subscribers (consumed by Newsletter.astro)
CREATE TABLE IF NOT EXISTS newsletter_subscribers (
  id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  email       TEXT NOT NULL UNIQUE,
  source      TEXT DEFAULT 'home',
  created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Contact form submissions (consumed by contact.astro)
CREATE TABLE IF NOT EXISTS contact_submissions (
  id            BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name          TEXT,
  email         TEXT,
  message       TEXT,
  inquiry_type  TEXT,
  submitted_at  TIMESTAMPTZ DEFAULT NOW()
);

-- Row Level Security (RLS)
-- Enable RLS on both tables and create insert-only policies for anon key:
ALTER TABLE newsletter_subscribers ENABLE ROW LEVEL SECURITY;
ALTER TABLE contact_submissions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow public inserts" ON newsletter_subscribers
  FOR INSERT TO anon WITH CHECK (true);

CREATE POLICY "Allow public inserts" ON contact_submissions
  FOR INSERT TO anon WITH CHECK (true);
