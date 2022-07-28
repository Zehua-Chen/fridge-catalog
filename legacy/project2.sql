-- Composite Types
CREATE TYPE Location AS (
  street VARCHAR(20),
  city VARCHAR(20),
  state VARCHAR(20),
  zip INT
);
CREATE TYPE Temperature AS (value FLOAT, isF BOOLEAN);
-- Integrate Composite Types
ALTER TABLE Markets ALTER location TYPE Location USING ROW('', '', '', 0);
ALTER TABLE Compartments ALTER temperature TYPE Temperature USING ROW(temperature, TRUE);
-- Arrays
ALTER TABLE Markets
ADD channels VARCHAR(10) ARRAY;
ALTER TABLE Markets
ADD CONSTRAINT valid_channels CHECK (channels <@ '{in-store, pickup, delivery}');
-- Triggers
CREATE FUNCTION delete_preparation() RETURNS trigger AS $delete_preparation$ BEGIN
DELETE FROM Preparation
WHERE Preparation.method = OLD.method;
RETURN OLD;
END $delete_preparation$ LANGUAGE plpgsql;
CREATE TRIGGER CleanPreparations BEFORE DELETE on PreparationMethods FOR EACH ROW EXECUTE PROCEDURE delete_preparation();
