-- Address book data for use in various tests.
PRAGMA user_version = 1;

CREATE TABLE cards (uid TEXT PRIMARY KEY, localId INTEGER);
CREATE TABLE properties (card TEXT, name TEXT, value TEXT);
CREATE TABLE lists (uid TEXT PRIMARY KEY, localId INTEGER, name TEXT, nickName TEXT, description TEXT);
CREATE TABLE list_cards (list TEXT, card TEXT, PRIMARY KEY(list, card));

INSERT INTO cards (uid, localId) VALUES
  ('420a2534-7e35-45e3-88b1-104e92608faa', 1),
  ('3291e9a7-cbd9-4146-9c4e-e1afe5e25085', 2),
  ('fcc46367-7081-487d-bbd3-f8f8e03e5262', 3),
  ('e62f6ec2-8248-478e-8f6d-e31cdbeda4b8', 4),
  ('4bc4f8c2-66d4-4421-a7b4-4be9d8be8614', 5);

INSERT INTO properties (card, name, value) VALUES
  ('420a2534-7e35-45e3-88b1-104e92608faa', 'PrimaryEmail', 'test1@com.invalid'),
  ('420a2534-7e35-45e3-88b1-104e92608faa', 'LowercasePrimaryEmail', 'test1@com.invalid'),
  ('420a2534-7e35-45e3-88b1-104e92608faa', 'PreferMailFormat', '0'),
  ('420a2534-7e35-45e3-88b1-104e92608faa', 'PopularityIndex', '0'),
  ('420a2534-7e35-45e3-88b1-104e92608faa', 'AllowRemoteContent', '0'),
  ('420a2534-7e35-45e3-88b1-104e92608faa', 'LastModifiedDate', '0'),

  ('3291e9a7-cbd9-4146-9c4e-e1afe5e25085', 'PrimaryEmail', 'test2@com.invalid'),
  ('3291e9a7-cbd9-4146-9c4e-e1afe5e25085', 'LowercasePrimaryEmail', 'test2@com.invalid'),
  ('3291e9a7-cbd9-4146-9c4e-e1afe5e25085', 'PreferMailFormat', '0'),
  ('3291e9a7-cbd9-4146-9c4e-e1afe5e25085', 'PopularityIndex', '0'),
  ('3291e9a7-cbd9-4146-9c4e-e1afe5e25085', 'AllowRemoteContent', '0'),
  ('3291e9a7-cbd9-4146-9c4e-e1afe5e25085', 'LastModifiedDate', '0'),

  ('fcc46367-7081-487d-bbd3-f8f8e03e5262', 'PrimaryEmail', 'test3@com.invalid'),
  ('fcc46367-7081-487d-bbd3-f8f8e03e5262', 'LowercasePrimaryEmail', 'test3@com.invalid'),
  ('fcc46367-7081-487d-bbd3-f8f8e03e5262', 'PreferMailFormat', '0'),
  ('fcc46367-7081-487d-bbd3-f8f8e03e5262', 'PopularityIndex', '0'),
  ('fcc46367-7081-487d-bbd3-f8f8e03e5262', 'AllowRemoteContent', '0'),
  ('fcc46367-7081-487d-bbd3-f8f8e03e5262', 'LastModifiedDate', '0'),

  ('e62f6ec2-8248-478e-8f6d-e31cdbeda4b8', 'PrimaryEmail', 'test4@com.invalid'),
  ('e62f6ec2-8248-478e-8f6d-e31cdbeda4b8', 'LowercasePrimaryEmail', 'test4@com.invalid'),
  ('e62f6ec2-8248-478e-8f6d-e31cdbeda4b8', 'PreferMailFormat', '1'),
  ('e62f6ec2-8248-478e-8f6d-e31cdbeda4b8', 'PopularityIndex', '0'),
  ('e62f6ec2-8248-478e-8f6d-e31cdbeda4b8', 'AllowRemoteContent', '0'),
  ('e62f6ec2-8248-478e-8f6d-e31cdbeda4b8', 'LastModifiedDate', '0'),

  ('4bc4f8c2-66d4-4421-a7b4-4be9d8be8614', 'PrimaryEmail', 'test5@com.invalid'),
  ('4bc4f8c2-66d4-4421-a7b4-4be9d8be8614', 'LowercasePrimaryEmail', 'test5@com.invalid'),
  ('4bc4f8c2-66d4-4421-a7b4-4be9d8be8614', 'PreferMailFormat', '2'),
  ('4bc4f8c2-66d4-4421-a7b4-4be9d8be8614', 'PopularityIndex', '0'),
  ('4bc4f8c2-66d4-4421-a7b4-4be9d8be8614', 'AllowRemoteContent', '0'),
  ('4bc4f8c2-66d4-4421-a7b4-4be9d8be8614', 'LastModifiedDate', '0');

INSERT INTO lists (uid, localId, name, nickName, description) VALUES
  ('df79d3c0-5976-4279-851c-a8814f17ef30', 1, 'ListTest1', '', ''),
  ('cad38149-925a-4159-8c34-20ac74ae7a17', 2, 'ListTest2', '', ''),
  ('c069dd7a-408f-4440-9fc0-67643fbe5777', 3, 'ListTest3', '', '');

INSERT INTO list_cards (list, card) VALUES
  ('df79d3c0-5976-4279-851c-a8814f17ef30', '420a2534-7e35-45e3-88b1-104e92608faa'),
  ('df79d3c0-5976-4279-851c-a8814f17ef30', '3291e9a7-cbd9-4146-9c4e-e1afe5e25085'),
  ('df79d3c0-5976-4279-851c-a8814f17ef30', 'fcc46367-7081-487d-bbd3-f8f8e03e5262'),
  ('cad38149-925a-4159-8c34-20ac74ae7a17', 'e62f6ec2-8248-478e-8f6d-e31cdbeda4b8'),
  ('c069dd7a-408f-4440-9fc0-67643fbe5777', '4bc4f8c2-66d4-4421-a7b4-4be9d8be8614');
