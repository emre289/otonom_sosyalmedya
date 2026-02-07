import React from "react";
import {Composition} from "remotion";
import {StoryVideo} from "./compositions/StoryVideo";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="StoryVideo"
        component={StoryVideo}
        durationInFrames={30 * 60}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          title: "Baslik Ornegi",
          subtitle: "Kisa aciklama burada",
          cards: [
            {start: 15, end: 120, title: "Kanca", body: "Ilk 3 saniyede vurgu"},
            {start: 150, end: 330, title: "Fayda", body: "Kisa ve net bilgi"},
            {start: 360, end: 540, title: "CTA", body: "Yorum at, takip et"}
          ],
          heygenVideoSrc: null,
          audioSrc: null
        }}
      />
    </>
  );
};
