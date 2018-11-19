function addition() {
//alert("Автор: Борисов Андрей Евгеньевич  \nВерсия: 1.0 ");

  //выбор арматуры
  //var armatura = document.getElementById('armatura_1').value;
  var armatura = $('#armatura_1').val()
  $('.armatura').html(armatura)

  //Спецификация колодца.
  // parseInt
  var dlina = parseInt($('#dlina').val())
  var shirina = parseInt($('#shirina').val())
  var vysota = parseInt($('#vysota').val())
  var tolshina_stenki = parseInt($('#tolshina_stenki').val())
  var gilza_1 = parseInt($('#gilza_1').val())
  var gilza_2 = parseInt($('#gilza_2').val())

  // Построение камеры (графическая визуализация)
  var canvas = document.getElementById('line');
  var obCanvas = canvas.getContext('2d');

  obCanvas.beginPath();
  obCanvas.lineWidth = 2;
  obCanvas.strokeStyle = 'green';
  obCanvas.moveTo(50, 50);
  obCanvas.lineTo(dlina/20, 50);
  obCanvas.lineTo(dlina/20, vysota/20);
  obCanvas.lineTo(50, vysota/20);
  obCanvas.lineTo(50, 50);
//  obCanvas.lineTo((dlina/20)/2+20, 2);
//  obCanvas.lineTo((dlina/20)/2+20, vysota/20-50);
//  obCanvas.lineTo(50, vysota/20);
  obCanvas.stroke();

  if (isNaN(dlina)==true) dlina=0;
  if (isNaN(shirina)==true) shirina=0;
  if (isNaN(vysota)==true) vysota=0;

  var dlina_poz_1 = dlina - 70;
  var dlina_poz_2 = shirina - 70;
  var dlina_poz_3 = 1200;
  var dlina_poz_4 = 1600;
  var dlina_poz_5 = dlina_poz_2;
  var dlina_poz_6 = dlina_poz_1;
  var dlina_poz_8 = vysota - 265;
  var dlina_poz_9 = 2000;
  var dlina_poz_10 = 1050;
  var dlina_poz_11 = 400;

  var kol_poz_1 = (Math.floor( ( dlina_poz_2 - 12 ) / 200 ) + 1) * 2 ;
  var kol_poz_2 = (Math.floor( ( dlina_poz_1 - 12 ) / 200 ) + 1) * 2 ;
  var kol_poz_3 = ( 1 * 4 ) + (Math.floor((dlina - tolshina_stenki * 2 - 12) / 200) + 1 ) * 2 + (Math.floor((shirina - tolshina_stenki * 2 - 12) / 200) + 1 ) * 2 + (Math.floor((vysota - tolshina_stenki - 212) / 200 ) + 1) * 4;
  var kol_poz_4 = ( 3 * 4 ) + (Math.floor((dlina - tolshina_stenki * 2 - 12) / 200) + 1 ) * 2 + (Math.floor((shirina - tolshina_stenki * 2 - 12) / 200) + 1 ) * 2 + (Math.floor((vysota - tolshina_stenki - 212) / 200 ) + 1) * 4;
  var kol_poz_5 = (Math.floor((vysota - tolshina_stenki - 212) / 200 ) + 1) * 4 ;
  var kol_poz_6 = kol_poz_5 ;
  var kol_poz_8 = ( 1 * 4 ) + (Math.floor((dlina - tolshina_stenki * 2 - 12) / 200) + 1 ) * 2 + (Math.floor((shirina - tolshina_stenki * 2 - 12) / 200) + 1 ) * 2 + ( 3 * 4 ) + (Math.floor((dlina - tolshina_stenki * 2 - 12) / 200) + 1 ) * 2 + (Math.floor((shirina - tolshina_stenki * 2 - 12) / 200) + 1 ) * 2 ;
  var kol_poz_9 = 4 ;
  var kol_poz_10 = (dlina / 1000 * shirina / 1000) * 2 ;
  var kol_poz_11 = Math.floor((((dlina * 2) / 1000) + ((shirina *2) / 1000) * (vysota / 1000 - 0.3)) * 12) ;

  //условие при котором выбирается масса ариатуры на п.м. в зависимости от диаметра.
  var arm_diam = 0;
  if (armatura == 12 ) {
    arm_diam = 0.888;
    ///alert( arm_diam );
  }
  else if (armatura == 14 ) {
    arm_diam = 1.21;
    //alert( arm_diam );
   }
  else if (armatura == 16 ) {
    arm_diam = 1.58;
    //alert( arm_diam );
   }

  //вывод значений в спец
  var massa_ed_poz_1 = (arm_diam * dlina_poz_1 / 1000).toFixed(2);
  var massa_ed_poz_2 = (arm_diam * dlina_poz_2 / 1000).toFixed(2);
  var massa_ed_poz_3 = (arm_diam * dlina_poz_3 / 1000).toFixed(2);
  var massa_ed_poz_4 = (arm_diam * dlina_poz_4 / 1000).toFixed(2);
  var massa_ed_poz_5 = (arm_diam * dlina_poz_5 / 1000).toFixed(2);
  var massa_ed_poz_6 = (arm_diam * dlina_poz_6 / 1000).toFixed(2);
  var massa_ed_poz_8 = (arm_diam * dlina_poz_8 / 1000).toFixed(2);
  var massa_ed_poz_9 = (arm_diam * dlina_poz_9 / 1000).toFixed(2);
  var massa_ed_poz_10 = (0.395 * dlina_poz_10 / 1000).toFixed(2);
  var massa_ed_poz_11 = (0.395 * dlina_poz_11 / 1000).toFixed(2);

  var massa_poz_1 = (massa_ed_poz_1 * kol_poz_1).toFixed(2);
  var massa_poz_2 = (massa_ed_poz_2 * kol_poz_2).toFixed(2);
  var massa_poz_3 = (massa_ed_poz_3 * kol_poz_3).toFixed(2);
  var massa_poz_4 = (massa_ed_poz_4 * kol_poz_4).toFixed(2);
  var massa_poz_5 = (massa_ed_poz_5 * kol_poz_5).toFixed(2);
  var massa_poz_6 = (massa_ed_poz_6 * kol_poz_6).toFixed(2);
  var massa_poz_8 = (massa_ed_poz_8 * kol_poz_8).toFixed(2);
  var massa_poz_9 = (massa_ed_poz_9 * kol_poz_9).toFixed(2);
  var massa_poz_10 = (massa_ed_poz_10 * kol_poz_10).toFixed(2);
  var massa_poz_11 = (massa_ed_poz_11 * kol_poz_11).toFixed(2);

  var massa_vsego = ( Number(massa_poz_1) + Number(massa_poz_2) + Number(massa_poz_3) +  Number(massa_poz_4) +  Number(massa_poz_5) +  Number(massa_poz_6)+ Number(massa_poz_8) +  Number(massa_poz_9) +  Number(massa_poz_10) +  Number(massa_poz_11)).toFixed(2);
  var obem_betona_B25 = (( dlina * shirina * vysota )  - (( dlina - tolshina_stenki*2 ) * ( shirina - tolshina_stenki*2 ) * ( vysota - 300 ))) / 1000000000  ;
  var obem_betona_B7_5 = (((( dlina + 200 ) * ( shirina + 200 )) / 1000000) * 0.1 ).toFixed(2);

  $('#dlina_poz_1').html(dlina_poz_1)
  $('#kol_poz_1').html(kol_poz_1)
  $('#massa_ed_poz_1').html(massa_ed_poz_1)
  $('#massa_poz_1').html(massa_poz_1)

  $('#dlina_poz_2').html(dlina_poz_2)
  $('#kol_poz_2').html(kol_poz_2)
  $('#massa_ed_poz_2').html(massa_ed_poz_2)
  $('#massa_poz_2').html(massa_poz_2)

  $('#dlina_poz_3').html(dlina_poz_3)
  $('#kol_poz_3').html(kol_poz_3)
  $('#massa_ed_poz_3').html(massa_ed_poz_3)
  $('#massa_poz_3').html(massa_poz_3)

  $('#dlina_poz_4').html(dlina_poz_4)
  $('#kol_poz_4').html(kol_poz_4)
  $('#massa_ed_poz_4').html(massa_ed_poz_4)
  $('#massa_poz_4').html(massa_poz_4)

  $('#dlina_poz_5').html(dlina_poz_5)
  $('#kol_poz_5').html(kol_poz_5)
  $('#massa_ed_poz_5').html(massa_ed_poz_5)
  $('#massa_poz_5').html(massa_poz_5)

  $('#dlina_poz_6').html(dlina_poz_6)
  $('#kol_poz_6').html(kol_poz_6)
  $('#massa_ed_poz_6').html(massa_ed_poz_6)
  $('#massa_poz_6').html(massa_poz_6)

  $('#dlina_poz_8').html(dlina_poz_8)
  $('#kol_poz_8').html(kol_poz_8)
  $('#massa_ed_poz_8').html(massa_ed_poz_8)
  $('#massa_poz_8').html(massa_poz_8)

  $('#dlina_poz_9').html(dlina_poz_9)
  $('#kol_poz_9').html(kol_poz_9)
  $('#massa_ed_poz_9').html(massa_ed_poz_9)
  $('#massa_poz_9').html(massa_poz_9)

  $('#dlina_poz_10').html(dlina_poz_10)
  $('#kol_poz_10').html(kol_poz_10)
  $('#massa_ed_poz_10').html(massa_ed_poz_10)
  $('#massa_poz_10').html(massa_poz_10)

  $('#dlina_poz_11').html(dlina_poz_11)
  $('#kol_poz_11').html(kol_poz_11)
  $('#massa_ed_poz_11').html(massa_ed_poz_11)
  $('#massa_poz_11').html(massa_poz_11)


  $('#massa_vsego_arm').html(massa_vsego_arm)
  $('#obem_betona_B25').html(obem_betona_B25)
  $('#obem_betona_B7_5').html(obem_betona_B7_5)

  var obem_peska = obem_betona_B7_5 ;

                // Спецификация гидроизоляции.

  //Устройство внутренней гидроизоляции. (МОСГАЗовская).
  var ploschad_kam_vnut = ((dlina - 2 * tolshina_stenki) * (shirina - 2 * tolshina_stenki) * 2 + (vysota - tolshina_stenki) * (dlina - 2 * tolshina_stenki) * 2 + (vysota - tolshina_stenki) * (shirina - 2 * tolshina_stenki) * 2) / 1000000 ;
  var galtel = (dlina * 2 +shirina * 2) / 1000 ;
  var galtel_1 = galtel * 2.5 ;
  var pnajkon = ploschad_kam_vnut ;
  var pnajkon_1 = ploschad_kam_vnut * 6 ;

  document.getElementById(' ploschad_kam_vnut ').innerHTML = ploschad_kam_vnut ;
  document.getElementById(' galtel ').innerHTML = galtel ;
  document.getElementById(' galtel_1 ').innerHTML = galtel_1 ;
  document.getElementById(' pnajkon ').innerHTML = pnajkon ;
  document.getElementById(' pnajkon_1 ').innerHTML = pnajkon_1 ;

  //Устройство гидроизоляции ввода.
  var dlina_shtroby = 2 * (Math.PI * (gilza_1 + gilza_2) / 1000).toFixed(2) ;
  var zap_shtrob = dlina_shtroby ;
  var zap_shtrob_1 = zap_shtrob * 2 ;
  var nabuh_prof = dlina_shtroby ;
  var nabuh_prof_1 = dlina_shtroby *1.2 ;
  var polidek = dlina_shtroby ;
  var polidek_1 = dlina_shtroby * 500 ;

  document.getElementById(' dlina_shtroby ').innerHTML = dlina_shtroby ;
  document.getElementById(' zap_shtrob ').innerHTML = zap_shtrob ;
  document.getElementById(' zap_shtrob_1 ').innerHTML = zap_shtrob_1 ;
  document.getElementById(' nabuh_prof ').innerHTML = nabuh_prof ;
  document.getElementById(' nabuh_prof_1 ').innerHTML = nabuh_prof_1 ;
  document.getElementById(' polidek ').innerHTML = polidek ;
  document.getElementById(' polidek_1 ').innerHTML = polidek_1 ;

  //Устройство внешней гидроизоляции. (МОСГАЗовская)
  var ploschad_kam_0 = ((dlina * shirina) * 2 + (dlina * ( vysota + 230 ) ) * 2 + (shirina * ( vysota + 230 ) *2 ))  / 1000000 ;
  var plenka = (dlina * shirina) / 1000000 ;
  var geo_tekstil = ((dlina + 400) * (shirina + 400)) * 2 / 1000000 ;
  var pili_moch = ploschad_kam_0 ;
  var pili_moch_1 = (ploschad_kam_0 * 3.5).toFixed(2) ;
  var prof_01 = (dlina * 2 + shirina * 2) / 1000 ;
  var shnur = prof_01 ;
  var germ_sit = prof_01 ;
  var germ_sit_1 = prof_01 * 500 ;
  var peno_pol = ((dlina * shirina) + (dlina * ( vysota + 230 ) ) * 2 + (shirina * ( vysota + 230 ) *2 ))  / 1000000 ;
  var peno_pol_1 = (peno_pol * 2.5).toFixed(2) ;
  var pesoc_sit = obem_betona_B7_5 ; ;

  document.getElementById(' ploschad_kam_0 ').innerHTML = ploschad_kam_0 ;
  document.getElementById(' plenka ').innerHTML = plenka ;
  document.getElementById(' geo_tekstil ').innerHTML = geo_tekstil ;
  document.getElementById(' pili_moch ').innerHTML = pili_moch ;
  document.getElementById(' pili_moch_1 ').innerHTML = pili_moch_1 ;
  document.getElementById(' prof_01 ').innerHTML = prof_01 ;
  document.getElementById(' shnur ').innerHTML = shnur ;
  document.getElementById(' germ_sit ').innerHTML = germ_sit ;
  document.getElementById(' germ_sit_1 ').innerHTML = germ_sit_1 ;
  document.getElementById(' peno_pol ').innerHTML = peno_pol ;
  document.getElementById(' peno_pol_1 ').innerHTML = peno_pol_1 ;
  document.getElementById(' pesoc_sit ').innerHTML = pesoc_sit ;


  //Устройство внешней гидроизоляции. [для МГЭ]
  var plenka_MEG = plenka ;
  var ploschad_kam = ((dlina * shirina) * 2 + (dlina * ( vysota + 230 ) ) * 2 + (shirina * ( vysota + 230 ) *2 )) / 1000000 ; // гидроизоляция камеры
  var ploschad_bitum = ploschad_kam ;
  var bitum = (ploschad_kam * 0.3).toFixed(2) ;
  var ploschad_rul_gid = ploschad_kam ;
  var ploschad_rul_gid_1 = (ploschad_kam * 1.2).toFixed(2) ;
  var ploschad_rul_shpona = ((dlina * shirina) + (dlina * ( vysota + 230 ) ) * 2 + (shirina * ( vysota + 230 ) *2 )) / 1000000 ;
  var ploschad_rul_shpona_1 = (ploschad_rul_shpona * 1.2).toFixed(2);
  var prof = (dlina * 2 + shirina * 2) / 1000 ;
  var germ = prof ;
  var germ_1 = germ * 500 ;
  var bent_shnur = prof  ;

  $('#plenka_MEG').html(plenka_MEG)
  $('#ploschad_kam').html(ploschad_kam)
  $('#ploschad_bitum').html(ploschad_bitum)
  $('#bitum').html(bitum)
  $('#ploschad_rul_gid').html(ploschad_rul_gid)
  $('#ploschad_rul_gid_1').html(ploschad_rul_gid_1)
  $('#ploschad_rul_shpona').html(ploschad_rul_shpona)
  $('#ploschad_rul_shpona_1').html(ploschad_rul_shpona_1)
  $('#prof').html(prof)
  $('#germ').html(germ)
  $('#germ_1').html(germ_1)
  $('#bent_shnur').html(bent_shnur)
  $('#obem_peska').html(obem_peska)

}
