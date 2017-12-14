create trigger set_ocr_rna_2015_2016 after insert on rfs_actual
BEGIN
/*2015*/
update rfs_actual set actual_ocr = 0.63 where date='2015-01-31';
update rfs_actual set actual_ocr = 0.58 where date='2015-02-28';
update rfs_actual set actual_ocr = 0.50 where date='2015-03-31';
update rfs_actual set actual_ocr = 0.53 where date='2015-04-30';
update rfs_actual set actual_ocr = 0.60 where date='2015-05-31';
update rfs_actual set actual_ocr = 0.42 where date='2015-06-30';
update rfs_actual set actual_ocr = 0.52 where date='2015-07-31';
update rfs_actual set actual_ocr = 0.53 where date='2015-08-31';
update rfs_actual set actual_ocr = 0.45 where date='2015-09-30';
update rfs_actual set actual_ocr = 0.47 where date='2015-10-31';
update rfs_actual set actual_ocr = 0.56 where date='2015-11-30';
update rfs_actual set actual_ocr = 0.76 where date='2015-12-31';

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
update rfs_actual set actual_rna = 0.63 where date='2015-12-31';
update rfs_actual set actual_rna = 8091 where date='2015-11-30';

/*2016*/
update rfs_actual set actual_ocr = 0.63 where date='2016-01-31';
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
update rfs_actual set actual_ocr = 0.65 where date='2016-12-31';

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
update rfs_actual set actual_rna = 7800 where date='2016-12-31';
update rfs_actual set actual_rna = 8060 where date='2016-11-30';
END;
create trigger set_revpar after update on rfs_actual
begin
update rfs_actual set actual_revpar = (actual_arr/actual_ocr) where actual_id = OLD.actual_id;
end ;