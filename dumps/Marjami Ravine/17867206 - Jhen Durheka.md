# 17867206 - Jhen Durheka

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Marjami Ravine (ID: 266) |
| Block Size       | 380 bytes                |
| Total Events     | 5                        |
| References Count | 18                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [45](#event-45)       | 0x0001       |     43 |              9 |
| [46](#event-46)       | 0x002C       |    109 |             31 |
| [47](#event-47)       | 0x0099       |     43 |              9 |
| [48](#event-48)       | 0x00C4       |     74 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x1E94      |        7828 |
|       2 | 0x1E95      |        7829 |
|       3 | 0x1E96      |        7830 |
|       4 | 0x0001      |           1 |
|       5 | 0x0000      |           0 |
|       6 | 0x1E98      |        7832 |
|       7 | 0x1E99      |        7833 |
|       8 | 0x094E      |        2382 |
|       9 | 0x1E9A      |        7834 |
|      10 | 0x1E9B      |        7835 |
|      11 | 0x1E9C      |        7836 |
|      12 | 0x1E97      |        7831 |
|      13 | 0x1E9D      |        7837 |
|      14 | 0x1E9E      |        7838 |
|      15 | 0x1E9F      |        7839 |
|      16 | 0x1EA0      |        7840 |
|      17 | 0x00C9      |         201 |

## String References

- **7828**: Numerous Velkk clans rrreside in this area. I don't care how battleworn you are--don't let your guard down. That's when they strike.
- **7829**: Purrrsonally, I'd love to sink my claws into those Velkk around here and make a nice handbag, but I need a bit of help. You in?
- **7830**: Up for some Velkk skinning? [Bloody pulp, here I come!/Violence is never the answer.]
- **7831**: Oh, come on. You must have seen whole rrrivers of blood in your time. What's one more trickle? If you ever need your thirrrst satiated, I'll be right here.
- **7832**: Rrright! Let's get down to business. I'm Jhen Durheka, in charge of surveying water quality here.
- **7833**: Despite my grrruff demeanor, I'm more of a thinker than a fighter. Even my reflexes aren't enough to blitz past those Velkk in the way.
- **7834**: That's where you come in--assuming you can mangle anything that gets in your way. Take this $3 and procure samples at both the source and the mouth of the river, as well as at the Dho Gates.
- **7835**: The water, you see, flows down from the ravine here into the gates.
- **7836**: The Velkk aren't the only thing to look out for. The cliffs are steep, and the last thing I want is some pioneer bloodying up the grrround below. Now, off with you!
- **7837**: You got gunk in your ears? I need you to take samples upstream, downstream, and at the Dho Gates. Have at it before those Velkk decide to multiply!
- **7838**: Wow, you actually--I mean, I didn't expect that you-- Well, either way, you made it back in one piece! Now about that surrrveying...
- **7839**: Hmm...this is quite intrrriguing. Unlike Yorcia and Hennetiel, the water here is pure. The pollution in those areas must be coming from Cirdas Caverns.
- **7840**: You've been a biggerrr help than I thought--and you gave the Velkk a bit of a scare too! Here's a little something for your trouble.

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

### Event 45

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 66 00 80 F8 FF  ...tlk0...#f....
0020: FF 7F F8 FF FF 7F 74 6C  6B 32 21 00              ......tlk2!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7828*)
    → "Numerous Velkk clans rrreside in this area. I don't care how battleworn you are--don't let your guard down. That's when they strike."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
  7: 0x002A [0x21] END_EVENT
  8: 0x002B [0x00] END_REQSTACK()
```

### Event 46

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x002C    |
| Data Size    | 109 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      42 1E F0 FF              B...
0030: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0040: 6C 6B 30 1D 02 80 23 24  03 80 04 80 05 80 25 02  lk0...#$......%.
0050: 00 10 05 80 00 79 00 42  1D 06 80 23 1D 07 80 23  .....y.B...#...#
0060: 03 02 10 08 80 1D 09 80  23 1D 0A 80 23 1D 0B 80  ........#...#...
0070: 23 03 01 10 04 80 01 88  00 02 00 10 04 80 00 88  #...............
0080: 00 1D 0C 80 23 01 88 00  66 00 80 F8 FF FF 7F F8  ....#...f.......
0090: FF FF 7F 74 6C 6B 32 21  00                       ...tlk2!.       
```

#### Opcodes

```
  0: 0x002C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0033 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0034 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  5: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=7829*)
    → "Purrrsonally, I'd love to sink my claws into those Velkk around here and make a nice handbag, but I need a bit of help. You in?"
  6: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0047 [0x24] CREATE_DIALOG(message_id=7830*, default_option=1*, option_flags=0*)
    → "Up for some Velkk skinning? [Bloody pulp, here I come!/Violence is never the answer.]"
  8: 0x004E [0x25] WAIT_DIALOG_SELECT()
  9: 0x004F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0079
 10: 0x0057 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 11: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=7832*)
    → "Rrright! Let's get down to business. I'm Jhen Durheka, in charge of surveying water quality here."
 12: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=7833*)
    → "Despite my grrruff demeanor, I'm more of a thinker than a fighter. Even my reflexes aren't enough to blitz past those Velkk in the way."
 14: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0060 [0x03] Work_Zone[2] = 2382*
 16: 0x0065 [0x1D] PRINT_EVENT_MESSAGE(message_id=7834*)
    → "That's where you come in--assuming you can mangle anything that gets in your way. Take this $3 and procure samples at both the source and the mouth of the river, as well as at the Dho Gates."
 17: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=7835*)
    → "The water, you see, flows down from the ravine here into the gates."
 19: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=7836*)
    → "The Velkk aren't the only thing to look out for. The cliffs are steep, and the last thing I want is some pioneer bloodying up the grrround below. Now, off with you!"
 21: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0071 [0x03] Work_Zone[1] = 1*
 23: 0x0076 [0x01] GOTO 0x0088
 24: 0x0079 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0088
 25: 0x0081 [0x1D] PRINT_EVENT_MESSAGE(message_id=7831*)
    → "Oh, come on. You must have seen whole rrrivers of blood in your time. What's one more trickle? If you ever need your thirrrst satiated, I'll be right here."
 26: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0085 [0x01] GOTO 0x0088

SUBROUTINE_0088:
 28: 0x0088 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
 29: 0x0097 [0x21] END_EVENT
 30: 0x0098 [0x00] END_REQSTACK()
```

### Event 47

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             1E F0 FF FF 7F 6F 70           .....op
00A0: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
00B0: 0D 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
00C0: 6B 32 21 00                                       k2!.            
```

#### Opcodes

```
  0: 0x0099 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x009E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x009F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00A0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x00AF [0x1D] PRINT_EVENT_MESSAGE(message_id=7837*)
    → "You got gunk in your ears? I need you to take samples upstream, downstream, and at the Dho Gates. Have at it before those Velkk decide to multiply!"
  5: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00B3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
  7: 0x00C2 [0x21] END_EVENT
  8: 0x00C3 [0x00] END_REQSTACK()
```

### Event 48

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C4   |
| Data Size    | 74 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:             42 1E F0 FF  FF 7F 6F 70 66 00 80 F8      B.....opf...
00D0: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 0E 80 23 1D  .......tlk0...#.
00E0: 0F 80 23 1D 10 80 23 66  00 80 F8 FF FF 7F F8 FF  ..#...#f........
00F0: FF 7F 74 6C 6B 32 45 11  80 F8 FF FF 7F F8 FF FF  ..tlk2E.........
0100: 7F 71 73 74 63 05 80 03  01 10 04 80 21 00        .qstc.......!.  
```

#### Opcodes

```
  0: 0x00C4 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00C5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00CA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00CB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00CC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  5: 0x00DB [0x1D] PRINT_EVENT_MESSAGE(message_id=7838*)
    → "Wow, you actually--I mean, I didn't expect that you-- Well, either way, you made it back in one piece! Now about that surrrveying..."
  6: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00DF [0x1D] PRINT_EVENT_MESSAGE(message_id=7839*)
    → "Hmm...this is quite intrrriguing. Unlike Yorcia and Hennetiel, the water here is pure. The pollution in those areas must be coming from Cirdas Caverns."
  8: 0x00E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7840*)
    → "You've been a biggerrr help than I thought--and you gave the Velkk a bit of a scare too! Here's a little something for your trouble."
 10: 0x00E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00E7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
 12: 0x00F6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 13: 0x0107 [0x03] Work_Zone[1] = 1*
 14: 0x010C [0x21] END_EVENT
 15: 0x010D [0x00] END_REQSTACK()
```
