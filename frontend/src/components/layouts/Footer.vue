<template>
  <div class="footer-container p-8 bg-gray-100">
    <span class="src-code">
      Click to see source code in github:
      <a class="link text-red-400" href="#">
        Link
        <Icon type="logo-github" size="18" class="ml-1" />
      </a>
    </span>
    <p
      class="info text-gray-600"
    >This project is created by myself (Hasan Muzak) for learning & improving my fullstack development skills.</p>
    <p class="info text-purple-600 mb-2">Frameworks used :</p>
    <div class="flex flex-col text-center justify-center items-center">
      <div class="border rounded p-2 rounded bg-gray-300">
        <span class="used-frm block">Python : Django, Django REST (Backend)</span>
        <span class="used-frm block mt-1">Javascript : Vue.JS (Frontend)</span>
        <span class="used-frm block mt-1">CSS : TailwindCSS, Pure CSS</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.used-frm {
  font-weight: 600;
  font-size: 12px;
}
.info {
  font-weight: 600;
  font-size: 12px;
  text-align: center;
  margin-top: 6px;
}
.footer-container {
  margin-top: 16px;
}
.link {
  font-weight: 600;
  font-size: 14px;
}
.src-code {
  display: block;
  text-transform: capitalize;
  text-align: center;
  font-weight: 600;
  font-size: 13px;
}
</style>