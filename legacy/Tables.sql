CREATE TABLE Users(
  name VARCHAR(20),
  uid INT NOT NULL,
  PRIMARY KEY (uid)
);
CREATE TABLE Compartments(
  clevel INT NOT NULL CHECK(clevel >= 0),
  temperature FLOAT,
  PRIMARY KEY (clevel)
);
CREATE TABLE Markets(
  mname VARCHAR(50) NOT NULL,
  location VARCHAR(50),
  PRIMARY KEY (mname)
);
CREATE TABLE Items(
  name VARCHAR(50),
  iid INT NOT NULL,
  price FLOAT CHECK(price >= 0.0),
  amount INT CHECK(amount > 0),
  calories FLOAT CHECK(calories >= 0.0),
  purchase DATE,
  use_by DATE CHECK(use_by > purchase),
  clevel INT NOT NULL,
  mname VARCHAR(50) NOT NULL,
  PRIMARY KEY (iid),
  FOREIGN KEY (clevel) REFERENCES Compartments(clevel) ON DELETE NO ACTION,
  FOREIGN KEY (mname) REFERENCES Markets(mname) ON DELETE NO ACTION
);
CREATE TABLE Nutrients(
  nname VARCHAR(50) NOT NULL,
  PRIMARY KEY(nname)
);
CREATE TABLE PreparationMethods(
  method VARCHAR(50) NOT NULL,
  PRIMARY KEY (method)
);
CREATE TABLE Allergens(aname VARCHAR(50), PRIMARY KEY (aname));
-- Relationships
CREATE TABLE Ownership(
  uid INT,
  iid INT,
  share FLOAT CHECK(share > 0.0),
  PRIMARY KEY (uid, iid),
  FOREIGN KEY (uid) REFERENCES Users(uid),
  FOREIGN KEY (iid) REFERENCES Items(iid)
);
CREATE TABLE Consumes(
  uid INT,
  iid INT,
  amount FLOAT CHECK(amount > 0),
  PRIMARY KEY (uid, iid),
  FOREIGN KEY (uid) REFERENCES Users(uid),
  FOREIGN KEY (iid) REFERENCES Items(iid)
);
CREATE TABLE ContainsNutrient(
  iid INT,
  nname VARCHAR(50),
  PRIMARY KEY(iid, nname),
  FOREIGN KEY (iid) REFERENCES Items(iid),
  FOREIGN KEY (nname) REFERENCES Nutrients(nname)
);
CREATE TABLE ContainsAllergen(
  iid INT,
  aname VARCHAR(50),
  PRIMARY KEY (iid, aname),
  FOREIGN KEY (iid) REFERENCES Items(iid),
  FOREIGN KEY (aname) REFERENCES Allergens(aname)
);
CREATE TABLE Preparation(
  iid INT,
  method VARCHAR(50),
  PRIMARY KEY(iid, method),
  FOREIGN KEY(iid) REFERENCES Items(iid),
  FOREIGN KEY(method) REFERENCES PreparationMethods(method)
);
