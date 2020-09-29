<template>
  <div class="filter-container">
    <div class="checkbox-body">
      <h3 class="title flex items-center">
        <Icon type="md-play" class="mr-1" />Genre
      </h3>
      <CheckboxGroup
        class="flex custom-checkbox-group flex-col"
        v-model="filterData.genre"
      >
        <div class="flex flex-col w-auto md:w-full">
          <Checkbox class="mb-1 checkbox-item" label="action">
            <span>Action</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="adventure">
            <span>Adventure</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="animation">
            <span>Animation</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="comedy">
            <span>Comedy</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="crime">
            <span>Crime</span>
          </Checkbox>
        </div>
        <div class="flex flex-col w-auto md:w-full">
          <Checkbox class="mb-1 checkbox-item" label="documentary">
            <span>Documentary</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="drama">
            <span>Drama</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="family">
            <span>Family</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="fantasy">
            <span>Fantasy</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="horror">
            <span>Horror</span>
          </Checkbox>
        </div>
        <div class="flex flex-col w-auto md:w-full">
          <Checkbox class="mb-1 checkbox-item" label="mystery">
            <span>Mystery</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="romance">
            <span>Romance</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="sci-fi">
            <span>Sci-Fi</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="thriller">
            <span>Thriller</span>
          </Checkbox>
          <Checkbox class="mb-1 checkbox-item" label="western">
            <span>Western</span>
          </Checkbox>
        </div>
      </CheckboxGroup>
    </div>
    <div class="checkbox-body">
      <h3 class="title flex items-center mt-2">
        <Icon type="md-play" class="mr-1" />Resolution
      </h3>
      <CheckboxGroup class="flex flex-col" v-model="filterData.resolution.is_4k">
        <Checkbox class="mb-1 checkbox-item resolution-checkbox" label="1">
          <span>4K(2160p)</span>
        </Checkbox>
      </CheckboxGroup>
      <CheckboxGroup class="flex flex-col"  v-model="filterData.resolution.is_fullHD">
        <Checkbox class="mb-1 checkbox-item resolution-checkbox" label="1">
          <span>FullHD</span>
        </Checkbox>
      </CheckboxGroup>
      <CheckboxGroup class="flex flex-col" v-model="filterData.resolution.is_HD">
        <Checkbox class="mb-1 checkbox-item resolution-checkbox" label="1">
          <span>HD</span>
        </Checkbox>
      </CheckboxGroup>
    </div>
    <div class="checkbox-body">
      <h3 class="title flex items-center mt-2">
        <Icon type="md-play" class="mr-1" />Status
      </h3>
      <CheckboxGroup class="flex flex-col" v-model="filterData.status">
        <Checkbox class="mb-1 checkbox-item" label="movie">
          <span>Movie</span>
        </Checkbox>
        <Checkbox class="mb-1 checkbox-item" label="serie">
          <span>Serie</span>
        </Checkbox>
      </CheckboxGroup>
    </div>
    <div class="selectable-body">
      <h3 class="title flex items-center mt-2">
        <Icon type="md-play" class="mr-1" />IMDb
      </h3>
      <Select v-model="filterData.imdb" placeholder="Choose Imdb..." clearable>
        <Option :value="9">9+</Option>
        <Option :value="8.5">8.5+</Option>
        <Option :value="8">8+</Option>
        <Option :value="7.5">7.5+</Option>
        <Option :value="7">7+</Option>
        <Option :value="6.5">6.5+</Option>
        <Option :value="5.5">5.5+</Option>
      </Select>
    </div>
    <Button
      class="w-full mt-2 submit-btn"
      type="success"
      @click="fetch({filterData : filterData})"
    >
      Apply Filter
      <Icon type="md-checkmark" class="ml-1" />
    </Button>
  </div>
</template>

<script>

export default {
  data() {
    return {
      filterData: {
        resolution: {
          is_4k: [],
          is_fullHD: [],
          is_HD: [],
        },
        status: [],
        genre: [],
        imdb: [],
      },
    };
  },
  methods: {
    fetch:function(params){
      this.$store.state.currentPage=1;
      this.$store.commit('fetchFilteredData', params.filterData);
    }
  },
};
</script>

<style scoped>
.submit-btn {
  font-size: 13px;
}
.checkbox-item span {
  color: #a1a5ba;
  font-size: 13px;
}
.title {
  color: white;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 13px;
  margin-bottom: 8px;
}
.filter-container {
  background: #343746;
  padding: 6px 11px;
  border-radius: 4px;
}
@media screen and (max-width: 1024px) {
  .custom-checkbox-group {
    flex-direction: row;
    justify-content: space-between;
  }
}
@media screen and (max-width: 375px) {
  .checkbox-item span {
    font-size: 11px;
  }
}
@media screen and (max-width: 335px) {
  .checkbox-item span {
    font-size: 9px;
  }
}
</style>
