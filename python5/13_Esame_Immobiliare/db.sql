-- Creazione di tipi ENUM personalizzati
CREATE TYPE stato_enum AS ENUM ('LIBERO', 'OCCUPATO');
CREATE TYPE tipo_affitto_enum AS ENUM ('PARZIALE', 'TOTALE');

-- Creazione della tabella filiali
CREATE TABLE filiali (
    partita_iva VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    indirizzo_sede VARCHAR(255) NOT NULL,
    civico INT NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

-- Creazione della tabella case_in_vendita
CREATE TABLE case_in_vendita (
    catastale VARCHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(255) NOT NULL,
    numero_civico INT NOT NULL,
    piano INT NOT NULL,
    metri INT NOT NULL,
    vani INT NOT NULL,
    prezzo DECIMAL(12, 2) NOT NULL,
    stato stato_enum NOT NULL,
    filiale_proponente VARCHAR(11),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);

-- Creazione della tabella case_in_affitto
CREATE TABLE case_in_affitto (
    catastale VARCHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(255) NOT NULL,
    civico INT NOT NULL,
    tipo_affitto tipo_affitto_enum NOT NULL,
    bagno_personale BOOLEAN NOT NULL,
    prezzo_mensile DECIMAL(12, 2) NOT NULL,
    filiale_proponente VARCHAR(11),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);

-- Creazione della tabella vendite_casa
CREATE TABLE vendite_casa (
    catastale VARCHAR(20),
    data_vendita DATE NOT NULL,
    filiale_proponente VARCHAR(11),
    filiale_venditrice VARCHAR(11),
    prezzo_vendita DECIMAL(12, 2) NOT NULL,
    PRIMARY KEY (catastale, data_vendita),
    FOREIGN KEY (catastale) REFERENCES case_in_vendita(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva)
);

-- Creazione della tabella affitti_casa
CREATE TABLE affitti_casa (
    catastale VARCHAR(20),
    data_affitto DATE NOT NULL,
    filiale_proponente VARCHAR(11),
    filiale_venditrice VARCHAR(11),
    prezzo_affitto DECIMAL(12, 2) NOT NULL,
    durata_contratto INT NOT NULL,
    PRIMARY KEY (catastale, data_affitto),
    FOREIGN KEY (catastale) REFERENCES case_in_affitto(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva)
);
