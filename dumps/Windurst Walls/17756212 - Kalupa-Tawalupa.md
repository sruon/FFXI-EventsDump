# 17756212 - Kalupa-Tawalupa

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 344 bytes                |
| Total Events     | 15                       |
| References Count | 10                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     16 |              2 |
| [65535.3](#event-655353) | 0x0021       |     16 |              2 |
| [65535.4](#event-655354) | 0x0031       |      6 |              2 |
| [443](#event-443)        | 0x0037       |      1 |              1 |
| [65535.5](#event-655355) | 0x0038       |     14 |              4 |
| [298](#event-298)        | 0x0046       |     36 |             11 |
| [64](#event-64)          | 0x006A       |      1 |              1 |
| [66](#event-66)          | 0x006B       |     22 |              7 |
| [72](#event-72)          | 0x0081       |     29 |             10 |
| [75](#event-75)          | 0x009E       |      1 |              1 |
| [65535.6](#event-655356) | 0x009F       |     19 |              5 |
| [65535.7](#event-655357) | 0x00B2       |     19 |              5 |
| [77](#event-77)          | 0x00C5       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFEF21D  |  4294898205 |
|       2 | 0x1C967     |      117095 |
|       3 | 0xFFFFD8F0  |  4294957296 |
|       4 | 0x1ED9      |        7897 |
|       5 | 0x1C50      |        7248 |
|       6 | 0x1C56      |        7254 |
|       7 | 0x1C5A      |        7258 |
|       8 | 0x1C5F      |        7263 |
|       9 | 0x1C63      |        7267 |

## String References

- **7248**: Are you all right, sir? Don't try and force yourself to continue. It might make your throat worse!
- **7254**: Hey, did that honey help you to talk a little just now? Then it must be effective. Quick, bring him as much honey as we can find!
- **7258**: He's gone silent all of a sudden! What's wrong, oh great teacher?
- **7263**: Your tooth...?
- **7267**: Well, I guess a tooth-ache or two is to be expected when you go around eating that much honey. That's just nature's providence!
- **7897**: I hear that the beastmen are on the move in every region lately. Even though Windurst has amicable relations with our local beastmen, the Yagudo, we still can't be sure if or when we are going to get pulled back into a full-scale war.

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
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   f..........thk1
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32   f..........thk2
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0021 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0031  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    5E 69 64 6C 30 00                               ^idl0.         
```

#### Opcodes

```
  0: 0x0031 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      00                                  .        
```

#### Opcodes

```
  0: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          32 00 80 5A 00 01 80 02          2..Z....
0040: 80 03 80 5A 01 00                                 ...Z..          
```

#### Opcodes

```
  0: 0x0038 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003B [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-69.091*, Z=117.095*, Y=-10.000*
  2: 0x0043 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0045 [0x00] END_REQSTACK()
```

### Event 298

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 36 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   1E F0  FF FF 7F 6F 70 29 0B 34        .....op).4
0050: F0 0E 01 02 1D 04 80 23  29 0B 34 F0 0E 01 03 29  .......#).4....)
0060: 0B 34 F0 0E 01 04 20 00  21 00                    .4.... .!.      
```

#### Opcodes

```
  0: 0x0046 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x02)
  4: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=7897*)
    → "I hear that the beastmen are on the move in every region lately. Even though Windurst has amicable relations with our local beastmen, the Yagudo, we still can't be sure if or when we are going to get pulled back into a full-scale war."
  5: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0058 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x03)
  7: 0x005F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x04)
  8: 0x0066 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0068 [0x21] END_EVENT
 10: 0x0069 [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                00                           .     
```

#### Opcodes

```
  0: 0x006A [0x00] END_REQSTACK()
```

### Event 66

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 22 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   29 0B 34 F0 0E             ).4..
0070: 01 01 1D 05 80 23 29 0B  34 F0 0E 01 04 20 00 21  .....#).4.... .!
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x006B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x01)
  1: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=7248*)
    → "Are you all right, sir? Don't try and force yourself to continue. It might make your throat worse!"
  2: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0076 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x04)
  4: 0x007D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x007F [0x21] END_EVENT
  6: 0x0080 [0x00] END_REQSTACK()
```

### Event 72

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    1E F0 FF FF 7F 6F 70  29 0B 34 F0 0E 01 01 1D   .....op).4.....
0090: 06 80 23 29 0B 34 F0 0E  01 04 20 00 21 00        ..#).4.... .!.  
```

#### Opcodes

```
  0: 0x0081 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0086 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0087 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0088 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x01)
  4: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=7254*)
    → "Hey, did that honey help you to talk a little just now? Then it must be effective. Quick, bring him as much honey as we can find!"
  5: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0093 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x04)
  7: 0x009A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x009C [0x21] END_EVENT
  9: 0x009D [0x00] END_REQSTACK()
```

### Event 75

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            00                   . 
```

#### Opcodes

```
  0: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               29                 )
00A0: 0B 34 F0 0E 01 01 1D 07  80 23 29 0B 34 F0 0E 01  .4.......#).4...
00B0: 04 00                                             ..              
```

#### Opcodes

```
  0: 0x009F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x01)
  1: 0x00A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7258*)
    → "He's gone silent all of a sudden! What's wrong, oh great teacher?"
  2: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00AA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x04)
  4: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       29 0B 34 F0 0E 01  01 1D 08 80 23 29 0B 34    ).4.......#).4
00C0: F0 0E 01 04 00                                    .....           
```

#### Opcodes

```
  0: 0x00B2 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x01)
  1: 0x00B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7263*)
    → "Your tooth...?"
  2: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00BD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x04)
  4: 0x00C4 [0x00] END_REQSTACK()
```

### Event 77

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                1E F0 FF  FF 7F 6F 70 29 0B 34 F0       .....op).4.
00D0: 0E 01 01 1D 09 80 23 29  0B 34 F0 0E 01 04 20 00  ......#).4.... .
00E0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00C5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00CB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00CC [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x01)
  4: 0x00D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7267*)
    → "Well, I guess a tooth-ache or two is to be expected when you go around eating that much honey. That's just nature's providence!"
  5: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00D7 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x04)
  7: 0x00DE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00E0 [0x21] END_EVENT
  9: 0x00E1 [0x00] END_REQSTACK()
```
