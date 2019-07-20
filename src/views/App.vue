
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
 
<v-navigation-drawer style="position: fixed; z-index:1; width:350px; margin-top: 60px;" right>
  <v-list two-line>
  <v-card width="320" style="margin:auto">
        <v-img
          src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
          height="200px"
        >
        </v-img>

        <v-card-title primary-title>
          <div>
            <div class="headline">НИКНЕЙМ</div>
            <span class="grey--text">КАКОЙ-ТО СТАТУС</span>
          </div>
        </v-card-title>

        <v-card-actions>
          <v-btn flat>Share</v-btn>
          <v-btn flat color="purple">Explore</v-btn>
          <v-spacer></v-spacer>
          <v-btn icon @click="show = !show">
            <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
          </v-btn>
        </v-card-actions>

        <v-slide-y-transition>
          <v-card-text v-show="show">
            КАКИЕ-ТО ХАРАКТЕРИСТИКИ
          </v-card-text>
        </v-slide-y-transition>
      </v-card>
    <v-progress-circular
    style="top:20px; left:20px"
      :rotate="360"
      :size="100"
      :width="15"
      :value="value"
      color="4312AE"
    >
      {{ value }}
    </v-progress-circular>
    <v-progress-circular
    style="top:20px; left:30px"
      :rotate="360"
      :size="100"
      :width="15"
      :value="value"
      color="4312AE"
    >
      {{ value }}
    </v-progress-circular>
     <v-progress-circular
    style="top:20px; left:40px"
      :rotate="360"
      :size="100"
      :width="15"
      :value="value"
      color="4312AE"
    >
      {{ value }}
    </v-progress-circular>
  </v-list>
</v-navigation-drawer>

      <v-sheet height="650" id="calendar">
        <!-- now is normally calculated by itself, but to keep the calendar in this date range to view events -->
        <v-calendar
          ref="calendar"
          :now="today"
          :value="today"
          color="primary"
          type="week"
        >
          <template v-slot:dayHeader="{ date }">
            <template v-for="event in eventsMap[date]">
              <v-menu
                :key="event.title"
                v-model="event.open"
                full-width
                offset-x
              >
                <template v-slot:activator="{ on }">
                  <div
                    v-if="!event.time"
                    :key="event.title"
                    class="my-event"
                    v-on="on"
                    v-html="event.title"
                  ></div>
                </template>
                <v-card
                  color="grey lighten-4"
                  min-width="350px"
                  flat
                >
                  <v-toolbar
                    color="primary"
                    dark
                  >
                    <v-btn icon>
                      <v-icon>edit</v-icon>
                    </v-btn>
                    <v-toolbar-title v-html="event.title"></v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn icon>
                      <v-icon>favorite</v-icon>
                    </v-btn>
                    <v-btn icon>
                      <v-icon>more_vert</v-icon>
                    </v-btn>
                  </v-toolbar>
                  <v-card-title primary-title>
                    <span v-html="event.details"></span>
                  </v-card-title>
                  <v-card-actions>
                    <v-btn
                      flat
                      color="secondary"
                    >
                      Cancel
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-menu>
            </template>
          </template>

          <template v-slot:dayBody="{ date, timeToY, minutesToPixels }">
            <template v-for="event in eventsMap[date]">
              <!-- timed events -->
              <v-menu
                :key="event.title"
                v-model="event.open"
                full-width
                offset-x
              >
                <template v-slot:activator="{ on }">
                  <div
                    v-if="event.time"
                    v-ripple
                    :style="{ top: timeToY(event.time) + 'px', height: minutesToPixels(event.duration) + 'px' }"
                    class="my-event with-time"
                    v-on="on"
                    v-html="event.title"
                  ></div>
                </template>
                <v-card
                  color="grey lighten-4"
                  min-width="350px"
                  flat
                >
                  <v-toolbar
                    color="primary"
                    dark
                  >
                    <v-btn icon>
                      <v-icon>edit</v-icon>
                    </v-btn>
                    <v-toolbar-title v-html="event.title"></v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn icon>
                      <v-icon>favorite</v-icon>
                    </v-btn>
                    <v-btn icon>
                      <v-icon>more_vert</v-icon>
                    </v-btn>
                  </v-toolbar>
                  <v-card-title primary-title>
                    <span v-html="event.details"></span>
                  </v-card-title>
                  <v-card-actions>
                    <v-btn
                      flat
                      color="secondary"
                    >
                      Cancel
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-menu>

            </template>
          </template>

        </v-calendar>
      </v-sheet>
      
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
</style>