<script>
  import Router from "svelte-spa-router";
  import Home from "./routes/Home.svelte";
  import UserLogin from "./routes/UserLogin.svelte";
  import MyPage from "./routes/MyPage.svelte";
  import BirthdayDetail from "./routes/BirthdayDetail.svelte";

  const routes = {
    "/": Home,
    "/user-login": UserLogin,
    "/my-page": MyPage,
    "/birthday-detail/:birthday_id": BirthdayDetail,
  };
</script>

<Router {routes} />
