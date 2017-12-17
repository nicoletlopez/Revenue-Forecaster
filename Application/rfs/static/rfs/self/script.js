function init_echarts() {

if( typeof (echarts) === 'undefined'){ return; }
console.log('init_echarts');


  var theme = {
  color: [
      '#26B99A', '#34495E', '#BDC3C7', '#3498DB',
      '#9B59B6', '#8abb6f', '#759c6a', '#bfd3b7'
  ],

  title: {
      itemGap: 8,
      textStyle: {
          fontWeight: 'normal',
          color: '#408829'
      }
  },

  dataRange: {
      color: ['#1f610a', '#97b58d']
  },

  toolbox: {
      color: ['#408829', '#408829', '#408829', '#408829']
  },

  tooltip: {
      backgroundColor: 'rgba(0,0,0,0.5)',
      axisPointer: {
          type: 'line',
          lineStyle: {
              color: '#408829',
              type: 'dashed'
          },
          crossStyle: {
              color: '#408829'
          },
          shadowStyle: {
              color: 'rgba(200,200,200,0.3)'
          }
      }
  },

  dataZoom: {
      dataBackgroundColor: '#eee',
      fillerColor: 'rgba(64,136,41,0.2)',
      handleColor: '#408829'
  },
  grid: {
      borderWidth: 0
  },

  categoryAxis: {
      axisLine: {
          lineStyle: {
              color: '#408829'
          }
      },
      splitLine: {
          lineStyle: {
              color: ['#eee']
          }
      }
  },

  valueAxis: {
      axisLine: {
          lineStyle: {
              color: '#408829'
          }
      },
      splitArea: {
          show: true,
          areaStyle: {
              color: ['rgba(250,250,250,0.1)', 'rgba(200,200,200,0.1)']
          }
      },
      splitLine: {
          lineStyle: {
              color: ['#eee']
          }
      }
  },
  timeline: {
      lineStyle: {
          color: '#408829'
      },
      controlStyle: {
          normal: {color: '#408829'},
          emphasis: {color: '#408829'}
      }
  },

  k: {
      itemStyle: {
          normal: {
              color: '#68a54a',
              color0: '#a9cba2',
              lineStyle: {
                  width: 1,
                  color: '#408829',
                  color0: '#86b379'
              }
          }
      }
  },
  map: {
      itemStyle: {
          normal: {
              areaStyle: {
                  color: '#ddd'
              },
              label: {
                  textStyle: {
                      color: '#c12e34'
                  }
              }
          },
          emphasis: {
              areaStyle: {
                  color: '#99d2dd'
              },
              label: {
                  textStyle: {
                      color: '#c12e34'
                  }
              }
          }
      }
  },
  force: {
      itemStyle: {
          normal: {
              linkStyle: {
                  strokeColor: '#408829'
              }
          }
      }
  },
  chord: {
      padding: 4,
      itemStyle: {
          normal: {
              lineStyle: {
                  width: 1,
                  color: 'rgba(128, 128, 128, 0.5)'
              },
              chordStyle: {
                  lineStyle: {
                      width: 1,
                      color: 'rgba(128, 128, 128, 0.5)'
                  }
              }
          },
          emphasis: {
              lineStyle: {
                  width: 1,
                  color: 'rgba(128, 128, 128, 0.5)'
              },
              chordStyle: {
                  lineStyle: {
                      width: 1,
                      color: 'rgba(128, 128, 128, 0.5)'
                  }
              }
          }
      }
  },
  gauge: {
      startAngle: 225,
      endAngle: -45,
      axisLine: {
          show: true,
          lineStyle: {
              color: [[0.2, '#86b379'], [0.8, '#68a54a'], [1, '#408829']],
              width: 8
          }
      },
      axisTick: {
          splitNumber: 10,
          length: 12,
          lineStyle: {
              color: 'auto'
          }
      },
      axisLabel: {
          textStyle: {
              color: 'auto'
          }
      },
      splitLine: {
          length: 18,
          lineStyle: {
              color: 'auto'
          }
      },
      pointer: {
          length: '90%',
          color: 'auto'
      },
      title: {
          textStyle: {
              color: '#333'
          }
      },
      detail: {
          textStyle: {
              color: 'auto'
          }
      }
  },
  textStyle: {
      fontFamily: 'Arial, Verdana, sans-serif'
  }
};


    if ($('#rev_revpar').length) {



    $(document).ready(function(){
    var revRevpar = echarts.init(document.getElementById('rev_revpar'), theme);
          var rev_total=[];
          var arr_total=[];
          var rns_total=[];
          var date=[];
          var pathname = window.location.pathname;
          var endpoint = '';
          if(pathname === '/rfs/project/2/'){
              endpoint = 'charts';
              alert(endpoint)
          }
          else if(pathname === '/rfs/project/2/individual/'){
              endpoint = 'ind_charts';
              alert(endpoint)
          }
          else if(pathname === '/rfs/project/2/group/'){
              endpoint = 'grp_charts';
              alert(endpoint)
          }
              $.ajax({
                  method: "GET",
                  url: endpoint,
                  success: function (data) {
                      rev_total = data.rev_total;
                      arr_total = data.arr_total;
                      rns_total = data.rns_total;
                      date = data.date;

                      revRevpar.setOption({
                          dataZoom: [
                              {
                                  type: 'slider',
                                  start: 0,
                                  end: 100
                              },
                              {
                                  type: 'inside',
                                  start: 0,
                                  end: 100
                              }
                          ],
                          title: {
                              text: 'RevPAR and Revenue Actual Data Graph',
                              subtext: ''
                          },
                          tooltip: {
                              trigger: 'axis'
                          },
                          legend: {
                              x: 220,
                              y: 40,
                              data: ['RevPAR', 'Revenue (\'000\'s)']
                          },
                          toolbox: {
                              show: true,
                              feature: {
                                  magicType: {
                                      show: true,
                                      title: {

                                          bar: 'Bar',
                                          line: 'Line',
                                          stack: 'Stack',
                                          tiled: 'Tiled'
                                      },
                                      type: ['bar', 'line', 'stack', 'tiled']
                                  },
                                  restore: {
                                      show: true,
                                      title: "Restore"
                                  },
                                  saveAsImage: {
                                      show: true,
                                      title: "Save Image"
                                  }
                              }
                          },
                          calculable: false,
                          xAxis: [{
                              type: 'category',
                              data: date
                          }],
                          yAxis: [{
                              type: 'value'
                          }],
                          series: [

                              {
                                  name: 'RevPAR',
                                  type: 'bar',
                                  smooth: true,
                                  itemStyle: {
                                      normal: {
                                          areaStyle: {
                                              type: 'default'
                                          }
                                      }
                                  },
                                  data: [100, 200, 300, 400, 500, 600, 700]
                              },
                              {
                                  name: 'Revenue (\'000\'s)',
                                  type: 'bar',
                                  smooth: true,
                                  itemStyle: {
                                      normal: {
                                          areaStyle: {
                                              type: 'default'
                                          }
                                      }
                                  },
                                  data: rev_total

                              }


                          ]
                      });
                  },
                  error: function (error_data) {
                      console.log("error");
                      console.log(error_data);
                  }
              })



    })
    }


    if ($('#arr_rns').length) {




    var arrRns = echarts.init(document.getElementById('arr_rns'), theme);

    arrRns.setOption({
    dataZoom: [
    {
    type: 'slider',
    start: 0,
    end: 100
    },
    {
    type: 'inside',
    start: 0,
    end: 100
    }
    ],
    title: {
        text: 'ARR and RNS Actual Data Graph',
        subtext: ''
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        x: 220,
        y: 40,
        data: ['Average Room Rate','Room Nights Sold']
    },
    toolbox: {
        show: true,
        feature: {
            magicType: {
                show: true,
                title: {

                    bar: 'Bar',
                    line: 'Line',
                    stack: 'Stack',
                    tiled: 'Tiled'
                },
                type: ['bar','line',  'stack', 'tiled']
            },
            restore: {
                show: true,
                title: "Restore"
            },
            saveAsImage: {
                show: true,
                title: "Save Image"
            }
        }
    },
    calculable: false,
    xAxis: [{
        type: 'category',
        data: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    }],
    yAxis: [{
        type: 'value'
    }],
    series: [

        {
        name:'Average Room Rate',
        type:'bar',
        smooth:true,
        itemStyle:{
            normal:{
                areaStyle:{
                    type:'default'
                }
            }
        },
        data:[100,200,300,400,500,600,700]
    },
        {
        name: 'Room Nights Sold',
        type: 'bar',
        smooth: true,
        itemStyle: {
            normal: {
                areaStyle: {
                    type: 'default'
                }
            }
        },
        data: [100,200,300,400,500,600,700]

    }



    ]
    });
    }


    if ($('#ocr').length) {




    var ocr = echarts.init(document.getElementById('ocr'), theme);

    ocr.setOption({
    dataZoom: [
    {
    type: 'slider',
    start: 0,
    end: 100
    },
    {
    type: 'inside',
    start: 0,
    end: 100
    }
    ],
    title: {
        text: 'Occupancy Rate Actual Data Graph',
        subtext: ''
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        x: 220,
        y: 40,
        data: ['RevPAR','Revenue (\'000\'s)']
    },
    toolbox: {
        show: true,
        feature: {
            magicType: {
                show: true,
                title: {

                    bar: 'Bar',
                    line: 'Line',
                    stack: 'Stack',
                    tiled: 'Tiled'
                },
                type: ['bar','line',  'stack', 'tiled']
            },
            restore: {
                show: true,
                title: "Restore"
            },
            saveAsImage: {
                show: true,
                title: "Save Image"
            }
        }
    },
    calculable: false,
    xAxis: [{
        type: 'category',
        data: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    }],
    yAxis: [{
        type: 'value'
    }],
    series: [

        {
        name:'Occupancy Rate',
        type:'bar',
        smooth:true,
        itemStyle:{
            normal:{
                areaStyle:{
                    type:'default'
                }
            }
        },
        data:[100,200,300,400,500,600,700]
    }



    ]
    });
              }

}