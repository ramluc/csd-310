drop USER if exists 'pysports_user'@'localhost';
create USER 'pysports_user'@'localhost' IDENTIFIED with mysql_native_password by '3512fred';
grant ALL PRIVLIGES on pysports.* TO'pysports_user'@'localhost';
drop table if exists player;
drop table if exists team;
create table team (
    team_id   int         not null   auto_increment,
    team_name varchar(75) not null,
    mascot    varchar(75) not null,
    primary key(team_id)
);
create table player (
    player_id  int         not null  auto_increment,
    first_name varchar(75) not null,
    last_name  varchar(75) not null,
    team_id    int         not null,
    primary key(player_id),
    constraint fk_team
    foreign key(team_id)
        references team(team_id)
);
insert into team(team_name,mascot)
    values('Team Gandalf','White Wizards');
insert into team(team_name,mascot)
    values('Team Balrog','Corrupted Maiar');

insert into player(first_name,last_name,team_id)
    values ('Gohn','Smith',Select team_id from team where team_name='Team Gandalf');
insert into player(first_name,last_name,team_id)
    values ('Gohnny','Test',Select team_id from team where team_name='Team Gandalf');
insert into player(first_name,last_name,team_id)
    values ('Gohnathon','Ricklebak',Select team_id from team where team_name='Team Gandalf');

insert into player(first_name,last_name,team_id)
    values ('Bohn','Rich',Select team_id from team where team_name='Team Balrog');
insert into player(first_name,last_name,team_id)
    values ('Bohnny','Susan',Select team_id from team where team_name='Team Balrog');
insert into player(first_name,last_name,team_id)
    values ('Bohnathon','Riddlesan',Select team_id from team where team_name='Team Balrog');
