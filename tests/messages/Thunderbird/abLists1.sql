-- Address book data for use in various tests.
PRAGMA user_version = 1;

CREATE TABLE cards (uid TEXT PRIMARY KEY, localId INTEGER);
CREATE TABLE properties (card TEXT, name TEXT, value TEXT);
CREATE TABLE lists (uid TEXT PRIMARY KEY, localId INTEGER, name TEXT, nickName TEXT, description TEXT);
CREATE TABLE list_cards (list TEXT, card TEXT, PRIMARY KEY(list, card));

INSERT INTO cards (uid, localId) VALUES
  ('0a64d642-7b51-4a84-be67-59b27ff2b528', 1),
  ('ce1bd5ad-17e7-4a1b-a51e-fbce76556ebd', 2),
  ('caaadb6c-425d-40e3-8f19-72546f6b01d8', 3),
  ('23acb230-f0d9-4348-a7be-1242cd579631', 4),
  ('02cf43d5-e5b8-48b4-9546-1bb509cd998f', 5);

INSERT INTO properties (card, name, value) VALUES
  ('0a64d642-7b51-4a84-be67-59b27ff2b528', 'PrimaryEmail', 'test1@foo.invalid'),
  ('0a64d642-7b51-4a84-be67-59b27ff2b528', 'LowercasePrimaryEmail', 'test1@foo.invalid'),
  ('0a64d642-7b51-4a84-be67-59b27ff2b528', 'PreferMailFormat', '0'),
  ('0a64d642-7b51-4a84-be67-59b27ff2b528', 'PopularityIndex', '0'),
  ('0a64d642-7b51-4a84-be67-59b27ff2b528', 'AllowRemoteContent', '0'),
  ('0a64d642-7b51-4a84-be67-59b27ff2b528', 'LastModifiedDate', '0'),

  ('ce1bd5ad-17e7-4a1b-a51e-fbce76556ebd', 'PrimaryEmail', 'test2@foo.invalid'),
  ('ce1bd5ad-17e7-4a1b-a51e-fbce76556ebd', 'LowercasePrimaryEmail', 'test2@foo.invalid'),
  ('ce1bd5ad-17e7-4a1b-a51e-fbce76556ebd', 'PreferMailFormat', '0'),
  ('ce1bd5ad-17e7-4a1b-a51e-fbce76556ebd', 'PopularityIndex', '0'),
  ('ce1bd5ad-17e7-4a1b-a51e-fbce76556ebd', 'AllowRemoteContent', '0'),
  ('ce1bd5ad-17e7-4a1b-a51e-fbce76556ebd', 'LastModifiedDate', '0'),

  ('caaadb6c-425d-40e3-8f19-72546f6b01d8', 'PrimaryEmail', 'test3@foo.invalid'),
  ('caaadb6c-425d-40e3-8f19-72546f6b01d8', 'LowercasePrimaryEmail', 'test3@foo.invalid'),
  ('caaadb6c-425d-40e3-8f19-72546f6b01d8', 'PreferMailFormat', '0'),
  ('caaadb6c-425d-40e3-8f19-72546f6b01d8', 'PopularityIndex', '0'),
  ('caaadb6c-425d-40e3-8f19-72546f6b01d8', 'AllowRemoteContent', '0'),
  ('caaadb6c-425d-40e3-8f19-72546f6b01d8', 'LastModifiedDate', '0'),

  ('23acb230-f0d9-4348-a7be-1242cd579631', 'PrimaryEmail', 'test4@foo.invalid'),
  ('23acb230-f0d9-4348-a7be-1242cd579631', 'LowercasePrimaryEmail', 'test4@foo.invalid'),
  ('23acb230-f0d9-4348-a7be-1242cd579631', 'LastModifiedDate', '1200685646'),
  ('23acb230-f0d9-4348-a7be-1242cd579631', 'PreferMailFormat', '1'),
  ('23acb230-f0d9-4348-a7be-1242cd579631', 'PopularityIndex', '0'),
  ('23acb230-f0d9-4348-a7be-1242cd579631', 'AllowRemoteContent', '0'),

  ('02cf43d5-e5b8-48b4-9546-1bb509cd998f', 'PrimaryEmail', 'test5@foo.invalid'),
  ('02cf43d5-e5b8-48b4-9546-1bb509cd998f', 'LowercasePrimaryEmail', 'test5@foo.invalid'),
  ('02cf43d5-e5b8-48b4-9546-1bb509cd998f', 'LastModifiedDate', '1200685651'),
  ('02cf43d5-e5b8-48b4-9546-1bb509cd998f', 'PreferMailFormat', '2'),
  ('02cf43d5-e5b8-48b4-9546-1bb509cd998f', 'PopularityIndex', '0'),
  ('02cf43d5-e5b8-48b4-9546-1bb509cd998f', 'AllowRemoteContent', '0');

INSERT INTO lists (uid, localId, name, nickName, description) VALUES
  ('98636844-ed9c-4ac1-98ac-de7989a93615', 1, 'TestList1', '', ''),
  ('31c44c28-450f-44d6-ba39-71cae90fac21', 2, 'TestList2', '', ''),
  ('46cf4cbf-5945-43e4-a822-30c2f2969db9', 3, 'TestList3', '', '');

INSERT INTO list_cards (list, card) VALUES
  ('98636844-ed9c-4ac1-98ac-de7989a93615', '0a64d642-7b51-4a84-be67-59b27ff2b528'),
  ('98636844-ed9c-4ac1-98ac-de7989a93615', 'ce1bd5ad-17e7-4a1b-a51e-fbce76556ebd'),
  ('98636844-ed9c-4ac1-98ac-de7989a93615', 'caaadb6c-425d-40e3-8f19-72546f6b01d8'),
  ('31c44c28-450f-44d6-ba39-71cae90fac21', '23acb230-f0d9-4348-a7be-1242cd579631'),
  ('46cf4cbf-5945-43e4-a822-30c2f2969db9', '02cf43d5-e5b8-48b4-9546-1bb509cd998f');
