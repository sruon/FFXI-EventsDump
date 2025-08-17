# 17756238 - Dabaide-Obaide

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 356 bytes                |
| Total Events     | 13                       |
| References Count | 10                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [316](#event-316)        | 0x0021       |     29 |             10 |
| [11](#event-11)          | 0x003E       |      1 |              1 |
| [47](#event-47)          | 0x003F       |     29 |             10 |
| [63](#event-63)          | 0x005C       |     29 |             10 |
| [167](#event-167)        | 0x0079       |     29 |             10 |
| [196](#event-196)        | 0x0096       |     29 |             10 |
| [247](#event-247)        | 0x00B3       |     33 |             12 |
| [204](#event-204)        | 0x00D4       |     29 |             10 |
| [532](#event-532)        | 0x00F1       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1EF9      |        7929 |
|       3 | 0x1C31      |        7217 |
|       4 | 0x1C4C      |        7244 |
|       5 | 0x1D29      |        7465 |
|       6 | 0x1D6F      |        7535 |
|       7 | 0x1DF4      |        7668 |
|       8 | 0x1DF5      |        7669 |
|       9 | 0x1D80      |        7552 |

## String References

- **7217**: Gee... An auction courier is a pretty dangerous job! It seems that every day you hear of another deliveryman getting attacked by some wild beasty-weasty or crazy customer.
- **7244**: Gee... I sure would like to meety-weety that summoner who appears in all the tales of twenty years ago. They say he was one of the great genius-weniuses who only appear once every several hundred years.
- **7465**: Gee... For safety's sake, I wouldn't recommend going-woing too close to Doctor Shantotto's manor! She thinks the whole world was made for her personal-wersonal pleasure.
- **7535**: Gee... That Professor Koru-Moru sure is a strange one. But what's even strangery-wangery is that they made him Principal of the School of Magic.
- **7552**: Gee... The other night when I looked up at the starry-warry sky, a trail of lighty-wighty went "wooshy-wooshy," streaming down to the ground. I think it would have hit the earthy-wearthy out there in West Sarutabaruta somewhere.
- **7668**: Gee... Everybody "nose" about the Rhinostery. That's the ministry-winistry that runs a biological laboratory to study plants and stuff.
- **7669**: Doctor Yoran-Oran used to be the Minister of the Rhinostery, but now he's retired-wetired and just vegetates here in Windurst Walls.
- **7929**: Gee... May the Goddess help us if a gossiper-wossiper like Ms. Mehruru ever became-ewame a lady-in-waiting. There'd be no secrets-wecrets left in Heavens Tower-wower!

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                92 01 F8 FF FF 7F            ......
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x001A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 316

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1E F0 FF FF 7F 6F 70  29 0B 4E F0 0E 01 01 1D   .....op).N.....
0030: 02 80 23 29 0B 4E F0 0E  01 02 20 00 21 00        ..#).N.... .!.  
```

#### Opcodes

```
  0: 0x0021 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0026 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0027 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0028 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x01)
  4: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=7929*)
    → "Gee... May the Goddess help us if a gossiper-wossiper like Ms. Mehruru ever became-ewame a lady-in-waiting. There'd be no secrets-wecrets left in Heavens Tower-wower!"
  5: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0033 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x02)
  7: 0x003A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x003C [0x21] END_EVENT
  9: 0x003D [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            00                   . 
```

#### Opcodes

```
  0: 0x003E [0x00] END_REQSTACK()
```

### Event 47

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               1E                 .
0040: F0 FF FF 7F 6F 70 29 0B  4E F0 0E 01 01 1D 03 80  ....op).N.......
0050: 23 29 0B 4E F0 0E 01 02  20 00 21 00              #).N.... .!.    
```

#### Opcodes

```
  0: 0x003F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0045 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0046 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x01)
  4: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7217*)
    → "Gee... An auction courier is a pretty dangerous job! It seems that every day you hear of another deliveryman getting attacked by some wild beasty-weasty or crazy customer."
  5: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0051 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x02)
  7: 0x0058 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x005A [0x21] END_EVENT
  9: 0x005B [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      1E F0 FF FF              ....
0060: 7F 6F 70 29 0B 4E F0 0E  01 01 1D 04 80 23 29 0B  .op).N.......#).
0070: 4E F0 0E 01 02 20 00 21  00                       N.... .!.       
```

#### Opcodes

```
  0: 0x005C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0062 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0063 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x01)
  4: 0x006A [0x1D] PRINT_EVENT_MESSAGE(message_id=7244*)
    → "Gee... I sure would like to meety-weety that summoner who appears in all the tales of twenty years ago. They say he was one of the great genius-weniuses who only appear once every several hundred years."
  5: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x006E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x02)
  7: 0x0075 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0077 [0x21] END_EVENT
  9: 0x0078 [0x00] END_REQSTACK()
```

### Event 167

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             1E F0 FF FF 7F 6F 70           .....op
0080: 29 0B 4E F0 0E 01 01 1D  05 80 23 29 0B 4E F0 0E  ).N.......#).N..
0090: 01 02 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x0079 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0080 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x01)
  4: 0x0087 [0x1D] PRINT_EVENT_MESSAGE(message_id=7465*)
    → "Gee... For safety's sake, I wouldn't recommend going-woing too close to Doctor Shantotto's manor! She thinks the whole world was made for her personal-wersonal pleasure."
  5: 0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x02)
  7: 0x0092 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0094 [0x21] END_EVENT
  9: 0x0095 [0x00] END_REQSTACK()
```

### Event 196

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0096   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   1E F0  FF FF 7F 6F 70 29 0B 4E        .....op).N
00A0: F0 0E 01 01 1D 06 80 23  29 0B 4E F0 0E 01 02 20  .......#).N.... 
00B0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0096 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x009B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x009C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x009D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x01)
  4: 0x00A4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7535*)
    → "Gee... That Professor Koru-Moru sure is a strange one. But what's even strangery-wangery is that they made him Principal of the School of Magic."
  5: 0x00A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A8 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x02)
  7: 0x00AF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00B1 [0x21] END_EVENT
  9: 0x00B2 [0x00] END_REQSTACK()
```

### Event 247

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          1E F0 FF FF 7F  6F 70 29 0B 4E F0 0E 01     .....op).N...
00C0: 01 1D 07 80 23 1D 08 80  23 29 0B 4E F0 0E 01 02  ....#...#).N....
00D0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x00B3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00BA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x01)
  4: 0x00C1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7668*)
    → "Gee... Everybody "nose" about the Rhinostery. That's the ministry-winistry that runs a biological laboratory to study plants and stuff."
  5: 0x00C4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7669*)
    → "Doctor Yoran-Oran used to be the Minister of the Rhinostery, but now he's retired-wetired and just vegetates here in Windurst Walls."
  7: 0x00C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00C9 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x02)
  9: 0x00D0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00D2 [0x21] END_EVENT
 11: 0x00D3 [0x00] END_REQSTACK()
```

### Event 204

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D4   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             1E F0 FF FF  7F 6F 70 29 0B 4E F0 0E      .....op).N..
00E0: 01 01 1D 09 80 23 29 0B  4E F0 0E 01 02 20 00 21  .....#).N.... .!
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00D9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00DA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00DB [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x01)
  4: 0x00E2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7552*)
    → "Gee... The other night when I looked up at the starry-warry sky, a trail of lighty-wighty went "wooshy-wooshy," streaming down to the ground. I think it would have hit the earthy-wearthy out there in West Sarutabaruta somewhere."
  5: 0x00E5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00E6 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dabaide-Obaide (ID: 17756238/0x010EF04E), tag_num=0x02)
  7: 0x00ED [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00EF [0x21] END_EVENT
  9: 0x00F0 [0x00] END_REQSTACK()
```

### Event 532

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F1  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x00F1 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00F7 [0x00] END_REQSTACK()
```
