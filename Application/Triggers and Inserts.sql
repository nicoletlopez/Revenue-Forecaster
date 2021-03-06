/*create table if not exists rfs_seg_list(id integer not null primary key AUTOINCREMENT , tag varchar(30) not null, name varchar(30) not null, seg_type varchar(30) not null,
  check(seg_type = 'GRP' or(seg_type = 'IND')));*/

/*trigger to populate child table ind_seg*/
CREATE TRIGGER if not exists insert_into_ind_seg after insert on rfs_seg_list
  when (new.seg_type = 'IND')
BEGIN
  insert into rfs_ind_seg values(new.id,new.tag,new.name);
END;

/*trigger to populate child table grp_seg*/
CREATE TRIGGER if not exists insert_into_grp_seg after insert on rfs_seg_list
  when (new.seg_type = 'GRP')
BEGIN
  insert into rfs_grp_seg values(new.id,new.tag,new.name);
END;

/*update TAG and NAME columns on ind_seg after update on parent table*/
CREATE TRIGGER if not exists update_seg_list_ind after update on rfs_seg_list
  when (new.seg_type = 'IND')
BEGIN
  update rfs_ind_seg set tag = new.tag, name = new.name where ind_id = new.id;
END;

/*update TAG and NAME columns on grp_seg after update on parent table*/
CREATE TRIGGER if not exists update_seg_list_grp after update on rfs_seg_list
  when (new.seg_type = 'IND')
BEGIN
  update rfs_grp_seg set tag = new.tag, name = new.name where grp_id = new.id;
END;

/*delete contents of ind)seg or grp_seg if delete is executed on parent table seg_list*/
CREATE TRIGGER if not exists delete_seg_list before delete on rfs_seg_list
BEGIN
  delete from rfs_ind_seg where ind_id = old.id;
  delete from rfs_grp_seg where grp_id = old.id;
END;

/*temporary trigger: set rna of each month of 2015-2016*/
create trigger if not exists set_ocr_rna_2015_2016 after insert on rfs_actual
BEGIN
/*2015*/

/*update rfs_actual set actual_ocr = 0.63 where date = '2015-01-31';
update rfs_actual set actual_ocr = 0.58 where date = '2015-02-28';
update rfs_actual set actual_ocr = 0.50 where date = '2015-03-31';
update rfs_actual set actual_ocr = 0.53 where date = '2015-04-30';
update rfs_actual set actual_ocr = 0.60 where date = '2015-05-31';
update rfs_actual set actual_ocr = 0.42 where date = '2015-06-30';
update rfs_actual set actual_ocr = 0.52 where date='2015-07-31';
update rfs_actual set actual_ocr = 0.53 where date='2015-08-31';
update rfs_actual set actual_ocr = 0.45 where date='2015-09-30';
update rfs_actual set actual_ocr = 0.47 where date='2015-10-31';
update rfs_actual set actual_ocr = 0.56 where date='2015-11-30';
update rfs_actual set actual_ocr = 0.76 where date='2015-12-31';*/


update rfs_actual set actual_rna = 8091 where date='2015-01-31';
update rfs_actual set actual_rna = 7308 where date='2015-02-28';
update rfs_actual set actual_rna = 8091 where date='2015-03-31';
update rfs_actual set actual_rna = 7830 where date='2015-04-30';
update rfs_actual set actual_rna = 8091 where date='2015-05-31';
update rfs_actual set actual_rna = 7830 where date='2015-06-30';
update rfs_actual set actual_rna = 8091 where date='2015-07-31';
update rfs_actual set actual_rna = 8091 where date='2015-08-31';
update rfs_actual set actual_rna = 7830 where date='2015-09-30';
update rfs_actual set actual_rna = 8091 where date='2015-10-31';
update rfs_actual set actual_rna = 7830 where date='2015-11-30';
update rfs_actual set actual_rna = 8091 where date='2015-12-31';

/*2016*/

/*update rfs_actual set actual_ocr = 0.63 where date='2016-01-31';
update rfs_actual set actual_ocr = 0.62 where date='2016-02-28';
update rfs_actual set actual_ocr = 0.53 where date='2016-03-31';
update rfs_actual set actual_ocr = 0.62 where date='2016-04-30';
update rfs_actual set actual_ocr = 0.50 where date='2016-05-31';
update rfs_actual set actual_ocr = 0.51 where date='2016-06-30';
update rfs_actual set actual_ocr = 0.50 where date='2016-07-31';
update rfs_actual set actual_ocr = 0.47 where date='2016-08-31';
update rfs_actual set actual_ocr = 0.49 where date='2016-09-30';
update rfs_actual set actual_ocr = 0.52 where date='2016-10-31';
update rfs_actual set actual_ocr = 0.58 where date='2016-11-30';
update rfs_actual set actual_ocr = 0.65 where date='2016-12-31';*/


update rfs_actual set actual_rna = 8091 where date='2016-01-31';
update rfs_actual set actual_rna = 7569 where date='2016-02-28';
update rfs_actual set actual_rna = 8091 where date='2016-03-31';
update rfs_actual set actual_rna = 7830 where date='2016-04-30';
update rfs_actual set actual_rna = 8056 where date='2016-05-31';
update rfs_actual set actual_rna = 7800 where date='2016-06-30';
update rfs_actual set actual_rna = 8060 where date='2016-07-31';
update rfs_actual set actual_rna = 8060 where date='2016-08-31';
update rfs_actual set actual_rna = 7800 where date='2016-09-30';
update rfs_actual set actual_rna = 8060 where date='2016-10-31';
update rfs_actual set actual_rna = 7800 where date='2016-11-30';
update rfs_actual set actual_rna = 8060 where date='2016-12-31';

END;

/*update occupancy rate if RNA is updated*/
create trigger if not exists update_ocr_after_rna_change after update of actual_rna on rfs_actual
  BEGIN
  update rfs_actual set actual_ocr = cast(cast(actual_rns as double precision)/cast(new.actual_rna as double precision) as double precision)
  where actual_id = old.actual_id;
  END;

/*update revpar if occupancy rate is updated*/
create trigger if not exists update_revpar_after_ocr_change after update of actual_ocr on rfs_actual
begin
  ---update rfs_actual set actual_ocr = (actual_rns/actual_rna) where actual_id = OLD.actual_id;
  update rfs_actual set actual_revpar = (actual_arr/actual_ocr) where actual_id = OLD.actual_id;
end ;

---create table rfs_ind_seg (ind_id integer primary key,tag varchar(30) not null,
  ---name varchar(30) not null, FOREIGN KEY (ind_id) REFERENCES rfs_seg_list(id));

/*create table rfs_grp_seg (grp_id integer primary key,tag varchar(30) not null,
  name varchar(30) not null, FOREIGN KEY (grp_id) REFERENCES  rfs_seg_list(id));*/


insert into rfs_seg_list (tag,name,seg_type) values('RCK','RACK','IND');
insert into rfs_seg_list (tag,name,seg_type) values('CORP','CORPORATE','IND');
insert into rfs_seg_list (tag,name,seg_type) values('CORPO','CORPORATE OTHERS','IND');
insert into rfs_seg_list (tag,name,seg_type) values('PKG/PRM','PACKAGES/PROMO','IND');
insert into rfs_seg_list (tag,name,seg_type) values('WSOL','WHOLESALE ONLINE','IND');
insert into rfs_seg_list (tag,name,seg_type) values('WSOF','WHOLESALE OFFLINE','IND');
insert into rfs_seg_list (tag,name,seg_type) values('INDO','INDIVIDUAL OTHERS','IND');
insert into rfs_seg_list (tag,name,seg_type) values('INDR','INDUSTRY RATE','IND');

insert into rfs_seg_list (tag,name,seg_type) values('CORPM','CORPORATE MEETINGS','GRP');
insert into rfs_seg_list (tag,name,seg_type) values('CON/ASSOC','CONVENTION/ASSOCIATION','GRP');
insert into rfs_seg_list (tag,name,seg_type) values('GOV''T/NGOS','GOV''T/NGOS','GRP');
insert into rfs_seg_list (tag,name,seg_type) values('GRPT','GROUP TOURS','GRP');
insert into rfs_seg_list (tag,name,seg_type) values('GRPO','GROUP OTHERS','GRP');
--insert into rfs_seg_list (tag,name,seg_type) values('BRT','BARTER','GRP');



