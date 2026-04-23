import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders';

const teamCollection = defineCollection({
  loader: file("src/content/team/members.json"),
  schema: z.object({
    name: z.string(),
    role: z.string(),
    bio: z.array(z.string()),
    photo: z.string(),
    group: z.enum(["leadership", "departmentHeads", "secretariat"]),
    linkedin: z.string().url().optional(),
  }),
});

const abstractsCollection = defineCollection({
  loader: file("src/content/abstracts/briefs.json"),
  schema: z.object({
    title: z.string(),
    publishedDate: z.string(),
    authors: z.array(z.string()),
    abstract: z.string(),
    tags: z.array(z.string()),
    sourceType: z.string(),
    externalURL: z.string().nullable(),
  }),
});

export const collections = {
  team: teamCollection,
  abstracts: abstractsCollection,
};
