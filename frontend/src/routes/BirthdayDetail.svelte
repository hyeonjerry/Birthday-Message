<script>
  import fastapi from "../lib/api";
  import { Fullpage, FullpageSection, FullpageSlide } from "svelte-fullpage";
  import moment from "moment/min/moment-with-locales";
  import Error from "../components/Error.svelte";
  moment.locale("ko");

  export let params = {};
  let birthday_id = params.birthday_id;
  let birthday = { name: "", bdate: "", introduce: "", messages: [] };
  let error = { detail: [] };
  let name = "";
  let message = "";

  function get_birthday() {
    fastapi("get", "/api/birthday/detail/" + birthday_id, {}, (json) => {
      birthday = json;
    });
  }

  function post_message(event) {
    event.preventDefault();
    let url = "/api/message/create/" + birthday_id;
    let params = {
      name: name,
      message: message,
    };
    fastapi(
      "post",
      url,
      params,
      (json) => {
        name = "";
        message = "";
        error = { detail: [] };
        get_birthday();
      },
      (err_json) => {
        error = err_json;
      }
    );
  }

  $: get_birthday();
</script>

<Fullpage>
  <FullpageSection
    class="bgimg"
    style="background-image: url(src/assets/bg1.jpg); background-position: center center;"
  >
    <div class="container text-center">
      <div class="row">
        <div class="col">
          <h1>
            {birthday.name}의 생일을 축하합니다🎉
          </h1>
          <p>
            {birthday.introduce}
          </p>
        </div>
      </div>
    </div>
  </FullpageSection>

  <FullpageSection
    class="bgimg"
    style="background-image: url(src/assets/donut.jpg);"
  >
    {#each birthday.messages as message}
      <FullpageSlide>
        <div class="container text-center">
          <div class="row">
            <div class="col">
              <h1>{message.message}</h1>
              <p>
                - {message.name}
              </p>
            </div>
          </div>
        </div>
      </FullpageSlide>
    {/each}
  </FullpageSection>

  <FullpageSection
    class="bgimg"
    style="background-image: url(src/assets/card.jpg);"
  >
    <div class="container text-center">
      <div class="row">
        <div class="col">
          <h1>축하 메시지 남기기📝</h1>

          <Error {error} />

          <form method="post" class="my-3">
            <div class="mb-3">
              <input
                type="text"
                class="form-control"
                bind:value={name}
                placeholder="닉네임"
              />
            </div>

            <div class="mb-3">
              <textarea
                class="form-control"
                bind:value={message}
                placeholder="축하 메시지"
                rows="3"
              />
            </div>

            <input
              type="submit"
              value="등록하기"
              class="btn btn-primary"
              on:click={post_message}
            />
          </form>
        </div>
      </div>
    </div>
  </FullpageSection>
</Fullpage>

<style>
  :global(body) {
    height: 100vh;
  }
  :global(#app) {
    height: 100%;
  }
  :global(.bgimg) {
    background-position: center center;
    background-size: cover;
  }
</style>
