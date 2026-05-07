class PromptTimelineSplitter:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "timeline_text": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "0-3s: man walking\n3-6s: enters cafe"
                    }
                ),
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "split_timeline"

    CATEGORY = "Timeline Tools"

    def split_timeline(self, timeline_text):

        lines = timeline_text.split("\n")

        output = []

        for line in lines:

            if ":" not in line:
                continue

            time_part, prompt_part = line.split(":", 1)

            output.append(
                f"TIME = {time_part.strip()} | PROMPT = {prompt_part.strip()}"
            )

        final_output = "\n".join(output)

        return (final_output,)


NODE_CLASS_MAPPINGS = {
    "PromptTimelineSplitter": PromptTimelineSplitter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptTimelineSplitter": "Prompt Timeline Splitter"
}