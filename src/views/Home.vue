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
    <v-list-tile v-for="item in items" :key='id' @click="">
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

<v-layout style="width:79%; margin-left:21%; margin-top: 2%" align-starts fill-height>
<template>
  <v-hover 
  v-for="obj in cardItems"
    :key="obj"
    
    >
    <v-card
      @click=""
      style="margin:0px; padding:0px;"
      slot-scope="{ hover }"
      class="mx-auto"
      color="grey lighten-4"
      width="500"
      height="400"
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
            Подробнее
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
        <h3 class="display-1 font-weight-light orange--text mb-2">{{obj.title}}</h3>     
      </v-card-text>
    </v-card>
  </v-hover>
</template>
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
       today: '2019-01-08',
      events: [
        {
          title: 'Weekly Meeting',
          date: '2019-01-07',
          time: '09:00',
          duration: 45,
          open:false
        },
        {
          title: 'Thomas\' Birthday',
          date: '2019-01-10',
          open:false
        },
        {
          title: 'Mash Potatoes',
          date: '2019-01-09',
          time: '12:30',
          duration: 180,
          open:false
        }
      ],
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
      items(){
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
          title:'математическое моделирование',
          teacher: 'Лолов Кек Чебурекович',
          host:'Дудаев',
          helpers:'Сидоров'
        },
         {
          title:'Информатика',
          teacher: 'Борщ Влад Мемов',
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

