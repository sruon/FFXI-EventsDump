# 17830098 - Ndah Tolohjin

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 432 bytes                 |
| Total Events     | 6                         |
| References Count | 17                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [508](#event-508)     | 0x0001       |     47 |             11 |
| [512](#event-512)     | 0x0030       |     43 |              9 |
| [2810](#event-2810)   | 0x005B       |    172 |             24 |
| [2519](#event-2519)   | 0x0107       |     60 |             18 |
| [5132](#event-5132)   | 0x0143       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x28DB      |       10459 |
|       2 | 0x28DC      |       10460 |
|       3 | 0x28DD      |       10461 |
|       4 | 0x08F0      |        2288 |
|       5 | 0x1E95      |        7829 |
|       6 | 0x1E96      |        7830 |
|       7 | 0x00C8      |         200 |
|       8 | 0x0000      |           0 |
|       9 | 0x1E97      |        7831 |
|      10 | 0x1E98      |        7832 |
|      11 | 0x00C9      |         201 |
|      12 | 0x1EE7      |        7911 |
|      13 | 0x1EE8      |        7912 |
|      14 | 0x1EE9      |        7913 |
|      15 | 0x1EEA      |        7914 |
|      16 | 0x1EEB      |        7915 |

## String References

- **7829**: Why, is that $6? Let me take a look... Oh, this is wonderrrful!
- **7830**: Well, well, this certainly was a pleasant surprrrise! I could give you a monetary reward, but instead, I'll give you something much better.
- **7831**: And a quick little stab herrre...t
- **7832**: Oh, don't be a baby. It's a vaccine that'll help you handle those pesky pungent fungi you pioneers've been having trrrouble with. Enjoy!
- **7911**: Hello, and welcome to the Scouts' Coalition, where we prrrovide you with the latest information!
- **7912**: Oh ho? Patrrrols? Everything is in tip-top condition here!
- **7913**: Our surveys of ergon loci and inspection of rrrare goods from Ulbuka are experiencing nothing but smooth sailing!
- **7914**: The Celennia Wexworth Memorial Library, under the purrrvey of our coalition, is also running without a hitch.
- **7915**: Taking some time to snuggle up with a good book is a grrreat way to spend the evening, don't you think?
- **10459**: You're on the hunt for a fleshless sort of prrrey? Well, our ears, eyes, and noses are the best in the reconnaissance business! That's why we're the Scouts' Coalition.
- **10460**: Hmmm... My sources tell me that the inforrrmation you seek can be obtained at the Pioneers' Coalition in Western Adoulin.
- **10461**: What's more imporrrtant than gil or bayld? Information! Looking for some facts to sink your teeth into or grab your arrrchnemesis by the throat with? Then step inside the Scouts' Coalition!

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 508

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 66  ...tlk0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 32 21 00  ..........tlk2!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10459*)
    → "You're on the hunt for a fleshless sort of prrrey? Well, our ears, eyes, and noses are the best in the reconnaissance business! That's why we're the Scouts' Coalition."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=10460*)
    → "Hmmm... My sources tell me that the inforrrmation you seek can be obtained at the Pioneers' Coalition in Western Adoulin."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 512

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 66  00 80 F8 FF FF 7F F8 FF  .....opf........
0040: FF 7F 74 6C 6B 30 1D 03  80 23 66 00 80 F8 FF FF  ..tlk0...#f.....
0050: 7F F8 FF FF 7F 74 6C 6B  32 21 00                 .....tlk2!.     
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=10461*)
    → "What's more imporrrtant than gil or bayld? Information! Looking for some facts to sink your teeth into or grab your arrrchnemesis by the throat with? Then step inside the Scouts' Coalition!"
  5: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
  7: 0x0059 [0x21] END_EVENT
  8: 0x005A [0x00] END_REQSTACK()
```

### Event 2810

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x005B    |
| Data Size    | 172 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   42 1E F0 FF FF             B....
0060: 7F 6F 70 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
0070: 6B 30 03 02 10 04 80 1D  05 80 23 1D 06 80 23 66  k0........#...#f
0080: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 32 45 07  ..........tlk2E.
0090: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 08 80 55  .........fdo1..U
00A0: 07 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 1D 09  ..........fdo1..
00B0: 80 23 45 07 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  .#E..........fdi
00C0: 31 08 80 55 07 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U..........fd
00D0: 69 31 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  i1f..........tlk
00E0: 30 1D 0A 80 23 66 00 80  F8 FF FF 7F F8 FF FF 7F  0...#f..........
00F0: 74 6C 6B 32 45 0B 80 F8  FF FF 7F F8 FF FF 7F 71  tlk2E..........q
0100: 73 74 63 08 80 21 00                              stc..!.         
```

#### Opcodes

```
  0: 0x005B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x005C [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0062 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  5: 0x0072 [0x03] Work_Zone[2] = 2288*
  6: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=7829*)
    → "Why, is that $6? Let me take a look... Oh, this is wonderrrful!"
  7: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x007B [0x1D] PRINT_EVENT_MESSAGE(message_id=7830*)
    → "Well, well, this certainly was a pleasant surprrrise! I could give you a monetary reward, but instead, I'll give you something much better."
  9: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x007F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
 11: 0x008E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x009F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 13: 0x00AE [0x1D] PRINT_EVENT_MESSAGE(message_id=7831*)
    → "And a quick little stab herrre...t"
 14: 0x00B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00B2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x00C3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 17: 0x00D2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
 18: 0x00E1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7832*)
    → "Oh, don't be a baby. It's a vaccine that'll help you handle those pesky pungent fungi you pioneers've been having trrrouble with. Enjoy!"
 19: 0x00E4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x00E5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
 21: 0x00F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 22: 0x0105 [0x21] END_EVENT
 23: 0x0106 [0x00] END_REQSTACK()
```

### Event 2519

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0107   |
| Data Size    | 60 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                      1E  F0 FF FF 7F 42 6F 70 66         .....Bopf
0110: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 0C  ..........tlk0..
0120: 80 23 1D 0D 80 23 1D 0E  80 23 1D 0F 80 23 1D 10  .#...#...#...#..
0130: 80 23 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#f..........tlk
0140: 32 21 00                                          2!.             
```

#### Opcodes

```
  0: 0x0107 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x010C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x010D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x010E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x010F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  5: 0x011E [0x1D] PRINT_EVENT_MESSAGE(message_id=7911*)
    → "Hello, and welcome to the Scouts' Coalition, where we prrrovide you with the latest information!"
  6: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0122 [0x1D] PRINT_EVENT_MESSAGE(message_id=7912*)
    → "Oh ho? Patrrrols? Everything is in tip-top condition here!"
  8: 0x0125 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0126 [0x1D] PRINT_EVENT_MESSAGE(message_id=7913*)
    → "Our surveys of ergon loci and inspection of rrrare goods from Ulbuka are experiencing nothing but smooth sailing!"
 10: 0x0129 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x012A [0x1D] PRINT_EVENT_MESSAGE(message_id=7914*)
    → "The Celennia Wexworth Memorial Library, under the purrrvey of our coalition, is also running without a hitch."
 12: 0x012D [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x012E [0x1D] PRINT_EVENT_MESSAGE(message_id=7915*)
    → "Taking some time to snuggle up with a good book is a grrreat way to spend the evening, don't you think?"
 14: 0x0131 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0132 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
 16: 0x0141 [0x21] END_EVENT
 17: 0x0142 [0x00] END_REQSTACK()
```

### Event 5132

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0143  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:          00                                          .            
```

#### Opcodes

```
  0: 0x0143 [0x00] END_REQSTACK()
```
