
CREATE TABLE votes (
    ipAddress varchar(16) not null,
    currentDate date not null,
    choice varchar(128) not null,
    primary key(ipAddress, currentDate)

) engine = innodb;