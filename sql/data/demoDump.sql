--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)


SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: playlists; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.playlists (
    playlist_id integer NOT NULL,
    title text NOT NULL,
    created_date text NOT NULL,
    details text,
    image_url text
);

ALTER TABLE public.playlists OWNER TO postgres;

CREATE SEQUENCE public.playlists_playlist_id_seq
    As integer
    START with 1 
    increment BY 1
    no MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.playlists_playlist_id_seq OWNER TO postgres;

ALTER SEQUENCE public.playlists_playlist_id_seq OWNED BY public.playlists.playlist_id;

--
-- Name: songs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.songs (
    song_id integer NOT NULL,
    title text NOT NULL,
    artist text NOT NULL,
    album text NOT NULL,
    duration int NOT NULL
);


ALTER TABLE public.songs OWNER TO postgres;

CREATE SEQUENCE public.songs_song_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.songs_song_id_seq OWNER TO postgres;

ALTER SEQUENCE public.songs_song_id_seq OWNED BY public.songs.song_id;

--
-- Name: connections; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.connections (
    connection_id integer NOT NULL,
    playlist_id integer NOT NULL,
    song_id integer NOT NULL
);


ALTER TABLE public.connections OWNER TO postgres;

CREATE SEQUENCE public.connections_connection_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.connections_connection_id_seq OWNER TO postgres;

ALTER SEQUENCE public.connections_connection_id_seq OWNED BY public.connections.connection_id;


ALTER TABLE ONLY public.playlists ALTER COLUMN playlist_id SET DEFAULT nextval('public.playlists_playlist_id_seq'::regclass);
ALTER TABLE ONLY public.songs ALTER COLUMN song_id SET DEFAULT nextval('public.songs_song_id_seq'::regclass);


--
-- Data for Name: playlists; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.playlists (playlist_id, title, created_date, details, image_url) FROM stdin;
1	"Classics Mix #1"	2023-01-25 10:31:49.601827	"Great for a karaoke night!"	"https://upload.wikimedia.org/wikipedia/commons/2/29/Funky_Stuff_mixtape.jpg"
2	"Jakob's study playlist"	2022-11-13 10:31:49.601827	"Time to get working."	"https://images.pexels.com/photos/1629212/pexels-photo-1629212.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
3	"Reggae favorites"	2022-07-12 10:31:49.601827	"Kick back and relax"	"https://i1.sndcdn.com/artworks-dRyfhz4WEjfnuYjD-9ssOXw-t500x500.jpg"
\.


--
-- Data for Name: songs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.songs (song_id, title, artist, album, duration) FROM stdin;
1	"Minute by Minute"	"The Doobie Brothers"	"Minute by Minute"	207
2	"If I Saw You Again"	"Pages"	"Pages"	205
3	"The Promise"	"When In Rome"	"When In Rome"	221
4	"Catch The Rainbow"	"Rainbow"	"Ritchie Blackmore's Rainbow"	396
5	"Shout"	"Tears For Fears"	"Songs From The Big Chair"	394
6	"Kiss on My List"	"Daryl Hall & John Oates"	"Voices"	265
7	"Vacuum"	"Gang Gang Dance"	"Saint Dymphna"	253
8	"Touched"	"my bloody valentine"	"Loveless"	57
9	"Press A Key"	"Plone"	"For Beginner Piano"	245
10	"Pulsewidth"	"Aphex Twin"	"Selected Ambient Works 85-92"	228
11	"Foil"	"Autechre"	"Amber"	365
12	"Introspection - Edit"	"Laraaji"	"Introspection (Edit)"	155
13	"dlp 1.3"	"William Basinski"	"The Disintegration Loops IV (Remastered)"	718
14	"I Shot The Sheriff"	"The Wailers"	"Burnin' (Deluxe Edition)"	280
15	"Concrete Jungle"	"Bob Marley & The Wailers"	"Catch A Fire"	254
16	"Your House"	"Steel Pulse"	"True Democracy"	223
17	"Under Mi Sensi"	"Barrington Levy"	"Too Experienced - The Best of Barrington Levy"	251
18	"Zungguzungguguzungguzeng"	"Yellowman"	"Zungguzungguguzungguzeng!"	388
19	"Dub Fire"	"Aswad"	"New Chapter Of Dub"	270
20	"Time Tough"	"Toots & The Maytals"	"Funky Kingston"	264
\.


--
-- Data for Name: songs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.connections (connection_id, playlist_id, song_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	2	7
8	2	8
9	2	9
10	2	10
11	2	11
12	2	12
13	2	13
14	3	14
15	3	15
16	3	16
17	3	17
18	3	18
19	3	19
20	3	20
\.

--
-- Name: offerlogs_offerlog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.playlists_playlist_id_seq', 1, false);
SELECT pg_catalog.setval('public.songs_song_id_seq', 1, false);
SELECT pg_catalog.setval('public.connections_connection_id_seq', 1, false);


--
-- Name: playlists playlists_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.playlists
    ADD CONSTRAINT playlists_pkey PRIMARY KEY (playlist_id);


--
-- Name: songs songs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.songs
    ADD CONSTRAINT songs_pkey PRIMARY KEY (song_id);


--
-- Name: connections connections_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.connections
    ADD CONSTRAINT connections_pkey PRIMARY KEY (connection_id);



--
-- Name: offerlogs offerlogs_asking_song_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.connections
    ADD CONSTRAINT connections_song_id_fkey FOREIGN KEY (song_id) REFERENCES public.songs(song_id) ON DELETE CASCADE;


--
-- Name: offerlogs offerlogs_owner_song_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.connections
    ADD CONSTRAINT connections_playlist_id_fkey FOREIGN KEY (playlist_id) REFERENCES public.playlists(playlist_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

