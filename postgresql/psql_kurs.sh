CREATE TABLE info (
  id uuid NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY, 
  login TEXT NOT NULL,
  password TEXT NOT NULL,
  img TEXT NOT NULL);

INSERT INTO info (login, password, img) VALUES ('test_user', '000', 'img');
