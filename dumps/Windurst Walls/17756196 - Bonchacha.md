# 17756196 - Bonchacha

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 292 bytes                |
| Total Events     | 9                        |
| References Count | 9                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [294](#event-294)        | 0x0030       |     39 |             13 |
| [65535.4](#event-655354) | 0x0057       |      1 |              1 |
| [202](#event-202)        | 0x0058       |     35 |             11 |
| [218](#event-218)        | 0x007B       |     39 |             13 |
| [229](#event-229)        | 0x00A2       |     39 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1ED2      |        7890 |
|       3 | 0x1ED3      |        7891 |
|       4 | 0x1D7E      |        7550 |
|       5 | 0x1DA2      |        7586 |
|       6 | 0x1DA3      |        7587 |
|       7 | 0x1DC4      |        7620 |
|       8 | 0x1DC5      |        7621 |

## String References

- **7550**: Oh, dearie-dear? Has that spot-dotty Professor Koru-Moru got you running errands for him now? Typical of old Principal Koru-Moru...totally dependent on the grace of others. Most precarious!
- **7586**: Goodness gracious. Has that utter nutter Professor Koru-Moru got you running errands again? What's it this time...?
- **7587**: Oh, burnite shells? You don't say...? Well, sorry. Never heard of them. Hoo-roo!
- **7620**: My, oh my. Does that crazy-lazy professor Koru-Moru have you out working for him again?
- **7621**: "Alchemy"? Sorry, Charlie, but I've never heard of that. Is it some kind of super-trooper magic?
- **7890**: Professor Koru-Moru, the old minister who lives in that manor there, is more famous for being the local ding-a-ling than for serving as the School of Magic's principal! I just know he's up to something in there!
- **7891**: I came over to call in and have a little chitchat, but it seems as if he is, how shall we say...otherwise occupied...?

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 1C 01 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x1C] WAIT(30* ticks)
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 294

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 86 00 F8 FF FF 7F 1E F0  FF FF 7F 6F 70 29 08 24  ...........op).$
0040: F0 0E 01 01 1D 02 80 23  1D 03 80 23 29 08 24 F0  .......#...#).$.
0050: 0E 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0030 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0036 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x003C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x003D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bonchacha (ID: 17756196/0x010EF024), tag_num=0x01)
  5: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=7890*)
    → "Professor Koru-Moru, the old minister who lives in that manor there, is more famous for being the local ding-a-ling than for serving as the School of Magic's principal! I just know he's up to something in there!"
  6: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=7891*)
    → "I came over to call in and have a little chitchat, but it seems as if he is, how shall we say...otherwise occupied...?"
  8: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bonchacha (ID: 17756196/0x010EF024), tag_num=0x02)
 10: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0055 [0x21] END_EVENT
 12: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0057  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      00                                  .        
```

#### Opcodes

```
  0: 0x0057 [0x00] END_REQSTACK()
```

### Event 202

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 35 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          86 00 F8 FF FF 7F 1E F0          ........
0060: FF FF 7F 6F 70 29 08 24  F0 0E 01 01 1D 04 80 23  ...op).$.......#
0070: 29 08 24 F0 0E 01 02 20  00 21 00                 ).$.... .!.     
```

#### Opcodes

```
  0: 0x0058 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x005E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0063 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0064 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0065 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bonchacha (ID: 17756196/0x010EF024), tag_num=0x01)
  5: 0x006C [0x1D] PRINT_EVENT_MESSAGE(message_id=7550*)
    → "Oh, dearie-dear? Has that spot-dotty Professor Koru-Moru got you running errands for him now? Typical of old Principal Koru-Moru...totally dependent on the grace of others. Most precarious!"
  6: 0x006F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0070 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bonchacha (ID: 17756196/0x010EF024), tag_num=0x02)
  8: 0x0077 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0079 [0x21] END_EVENT
 10: 0x007A [0x00] END_REQSTACK()
```

### Event 218

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   86 00 F8 FF FF             .....
0080: 7F 1E F0 FF FF 7F 6F 70  29 08 24 F0 0E 01 01 1D  ......op).$.....
0090: 05 80 23 1D 06 80 23 29  08 24 F0 0E 01 02 20 00  ..#...#).$.... .
00A0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x007B [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0081 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0086 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0087 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0088 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bonchacha (ID: 17756196/0x010EF024), tag_num=0x01)
  5: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=7586*)
    → "Goodness gracious. Has that utter nutter Professor Koru-Moru got you running errands again? What's it this time...?"
  6: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=7587*)
    → "Oh, burnite shells? You don't say...? Well, sorry. Never heard of them. Hoo-roo!"
  8: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0097 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bonchacha (ID: 17756196/0x010EF024), tag_num=0x02)
 10: 0x009E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x00A0 [0x21] END_EVENT
 12: 0x00A1 [0x00] END_REQSTACK()
```

### Event 229

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       86 00 F8 FF FF 7F  1E F0 FF FF 7F 6F 70 29    ...........op)
00B0: 08 24 F0 0E 01 01 1D 07  80 23 1D 08 80 23 29 08  .$.......#...#).
00C0: 24 F0 0E 01 02 20 00 21  00                       $.... .!.       
```

#### Opcodes

```
  0: 0x00A2 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x00A8 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00AD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00AE [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00AF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bonchacha (ID: 17756196/0x010EF024), tag_num=0x01)
  5: 0x00B6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7620*)
    → "My, oh my. Does that crazy-lazy professor Koru-Moru have you out working for him again?"
  6: 0x00B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00BA [0x1D] PRINT_EVENT_MESSAGE(message_id=7621*)
    → ""Alchemy"? Sorry, Charlie, but I've never heard of that. Is it some kind of super-trooper magic?"
  8: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00BE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bonchacha (ID: 17756196/0x010EF024), tag_num=0x02)
 10: 0x00C5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x00C7 [0x21] END_EVENT
 12: 0x00C8 [0x00] END_REQSTACK()
```
