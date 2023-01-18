<script>
  import Router from "svelte-spa-router";
  import Home from "./routes/Home.svelte";
  import UserLogin from "./routes/UserLogin.svelte";
  import MyPage from "./routes/MyPage.svelte";

  const routes = {
    "/": Home,
    "/user-login": UserLogin,
    "/my-page": MyPage,
  };
</script>

<Router {routes} />
