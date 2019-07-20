<template>
 
  <v-app>
    <v-toolbar color="primary" app style="z-index:2; background-color: teal;">
      <v-toolbar-side-icon color="primary" @click.stop="drawer=!drawer, resize(drawer)"></v-toolbar-side-icon>
      <v-toolbar-title ></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
    </v-toolbar-items> 
    </v-toolbar>
 
    <v-content>
          <v-navigation-drawer style="position: absolute;z-index:1" v-model="drawer">
  <v-list two-line flat>
    <v-list-tile v-for="item in  navs" :key='id' @click="">
      <router-link :to="item.router">
      <v-list-tile-action>
        <v-icon v-html="item.icon"></v-icon>
      </v-list-tile-action>
      <v-list-tile-content>
  <v-list-tile-title v-text="item.title"></v-list-tile-title> 
  </v-list-tile-content>
  </router-link>
    </v-list-tile>
  </v-list>
 
  </v-navigation-drawer>
 
 <v-layout style="width=80%;" right d-{flex} align-start justify-center row wrap>
           <v-hover
            v-for="obj in cardItems"
          :key="obj.id"
           >
            <v-card
          @click=""
          style="margin:10px;"        
       slot-scope="{ hover }"
      class="mx-auto"
      color="grey lighten-4"
      max-width="600"
    >
      <v-img
        :aspect-ratio="16/9"
        src="https://cdn.vuetifyjs.com/images/cards/kitchen.png"
      >
        <v-expand-transition>
          <div
            v-if="hover"
            class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-3 white--text"
            style="height: 100%;"
          >
            $14.99
          </div>
        </v-expand-transition>
      </v-img>
      <v-card-text
        class="pt-4"
        style="position: relative;"
      >
        <v-btn
          absolute
          color="orange"
          class="white--text"
          fab
          large
          right
          top
        >
          <v-icon>mdi-cart</v-icon>
        </v-btn>
        <div class="font-weight-light grey--text title mb-2">For the perfect meal</div>
        <h3 class="display-1 font-weight-light orange--text mb-2">QW cooking utensils</h3>
        <div class="font-weight-light title mb-2">
          Our Vintage kitchen utensils delight any chef.<br>
          Made of bamboo by hand
        </div>
      </v-card-text>
    </v-card>
  </v-hover>
        </v-card-title>

               <v-card-actions>
                 <template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" max-width="80%" max-height="100%">
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark v-on="on">Описание</v-btn>
      </template>
      <v-card>
        <v-layout justify-center>
          <span class="headline">{{obj.title}}</span><br>
        </v-layout>
          <v-timeline align-top>
    <v-timeline-item
      v-for="(item, i) in items"
      :key="i"
      :color="item.color"
      :icon="item.icon"
      fill-dot
    >
        <template v-slot:opposite>
        <span
          :class="'headline font-weight-bold ${item.color}--text'"
          v-text="item.name"
        ></span>
      </template>
      <v-card
        :color="item.color"
        dark
      >
        <v-card-title class="title">{{item.name}}</v-card-title>
        <v-card-text class="white text--primary">
          <p>{{item.description}}</p>
          <v-card-title><span class="headline">Авторы</span></v-card-title>
         <v-card-text v-for="author in item.authors">
          <span><v-icon color="accent">account_circle</v-icon>{{author}} </span>
          </v-card-text> 
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
   <v-card-actions>
<v-layout justify-center>
          <v-btn
            color="primary"
            flat
            @click="dialog = false"
          >
          Записаться
          </v-btn>
  </v-layout>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</v-content>
  </v-app>
</template>



<script>
export default {
  name: 'App',
  components: {
  },
  data () {
    return {
      items: [
        {
          name: "Базовые операции",
          description:"Равным образом дальнейшее развитие различных форм деятельности требуют от нас анализа системы обучения кадров, соответствует насущным потребностям. Таким образом начало повседневной работы по формированию позиции представляет собой интересный эксперимент проверки направлений прогрессивного развития.",
          authors:["Суворов","Кутузов"],
          color: 'red lighten-2',
          icon: 'mdi-star'
        },
        {
          name:"Введение в матанализ",
          description:"Равным образом дальнейшее развитие различных форм деятельности требуют от нас анализа системы обучения кадров, соответствует насущным потребностям. Таким образом начало повседневной работы по формированию позиции представляет собой интересный эксперимент проверки направлений прогрессивного развития.",
          color: 'purple darken-1',
          authors:["Суворов","Кутузов"],
          icon: 'mdi-book-variant'
        },
        {
          name:"Интегрирование",
          description:"Равным образом дальнейшее развитие различных форм деятельности требуют от нас анализа системы обучения кадров, соответствует насущным потребностям. Таким образом начало повседневной работы по формированию позиции представляет собой интересный эксперимент проверки направлений прогрессивного развития.",
          authors:["Суворов","Кутузов"],
          color: 'green lighten-1',

          icon: 'mdi-airballoon'
        },
        {
          name:"Моделирование",
          description:"Равным образом дальнейшее развитие различных форм деятельности требуют от нас анализа системы обучения кадров, соответствует насущным потребностям. Таким образом начало повседневной работы по формированию позиции представляет собой интересный эксперимент проверки направлений прогрессивного развития.",
          authors:["Суворов"],
          color: 'indigo',
          icon: 'mdi-buffer'
        }
      ],
       today: '2019-01-08',
      drawer:true,
      dialog:false,
      show: false,
      interval: {},
      value: 0
    }
  },
  computed: {
      // convert the list of events into a map of lists keyed by date
      eventsMap () {
        const map = {}
        this.events.forEach(e => (map[e.date] = map[e.date] || []).push(e))
        return map
      },
      navs(){
        return[
        {
          id:1,
          title:'ГЛАВНАЯ',
          icon:'widgets',
          router:'/Home'
        },
        {
          id:2,
          title:'МОЙ КАБИНЕТ',
          icon:'widgets',
          router:'/'
        },
        ]
      },
    cardItems(){
      return[
        {
          title:'Mатематическое моделирование',
          teacher: 'Лолов Кек Чебурекович',
          description:'Равным образом дальнейшее развитие различных форм деятельности требуют от нас анализа системы обучения кадров, соответствует насущным потребностям. Таким образом начало повседневной работы по формированию позиции представляет собой интересный эксперимент проверки направлений прогрессивного развития.',
          host:'Дудаев',
          helpers:'Сидоров'
        },
         {
          title:'Информатика',
          teacher: 'Борщ Влад Мемов',
          description:'Равным образом дальнейшее развитие различных форм деятельности требуют от нас анализа системы обучения кадров, соответствует насущным потребностям. Таким образом начало повседневной работы по формированию позиции представляет собой интересный эксперимент проверки направлений прогрессивного развития.',
          host:'Гаврилов',
          helpers:'Ололоев'
        }
      ]
    }
  },
    beforeDestroy () {
      clearInterval(this.interval)
    },
    mounted () {
      this.$refs.calendar.scrollToTime('08:00');
      this.interval = setInterval(() => {
        if (this.value === 100) {
          return (this.value = 0)
        }
        this.value += 5
      }, 1000)
    },
    methods: {
      open (event) {
        alert(event.title)
      },
      resize(drawer){
        if(!drawer)
        {
          document.getElementById('calendar').style="width:70%; height: 90%; left:40px; position:absolute; margin:auto;  margin-top:20px; ";
        }
        else
        {
          document.getElementById('calendar').style="width:50%; height: 90%; position:absolute; margin:auto;  margin-top:20px; margin-left: 23%; ";
        }
      }
    }
}
</script>
<style lang="stylus" scoped>
  .my-event {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border-radius: 2px;
    background-color: #FFDB00;
    color: #ffffff;
    border: 1px solid #FFDB00;
    font-size: 12px;
    padding: 3px;
    cursor: pointer;
    margin-bottom: 1px;
    left: 4px;
    margin-right: 8px;
    position: relative;
    &.with-time {
      position: absolute;
      right: 4px;
      margin-right: 0px;
    }
  }
  #calendar{
    margin-left: 23%; 
    z-index:0; 
    margin-top:20px; 
    position: absolute;
    width:50%;
    height:90%;
  }

.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: .5;
  position: absolute;
  width: 100%;
}

</style>

