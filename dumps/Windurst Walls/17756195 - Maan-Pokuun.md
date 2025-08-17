# 17756195 - Maan-Pokuun

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 300 bytes                |
| Total Events     | 11                       |
| References Count | 12                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [443](#event-443)        | 0x0030       |      7 |              2 |
| [65535.4](#event-655354) | 0x0037       |     14 |              4 |
| [293](#event-293)        | 0x0045       |     26 |              9 |
| [65535.5](#event-655355) | 0x005F       |      1 |              1 |
| [201](#event-201)        | 0x0060       |     29 |             10 |
| [220](#event-220)        | 0x007D       |     33 |             12 |
| [230](#event-230)        | 0x009E       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFEC029  |  4294885417 |
|       3 | 0x1E4A8     |      124072 |
|       4 | 0xFFFFEA0E  |  4294961678 |
|       5 | 0x1ECE      |        7886 |
|       6 | 0x1ECF      |        7887 |
|       7 | 0x1D7D      |        7549 |
|       8 | 0x1DA5      |        7589 |
|       9 | 0x1DA6      |        7590 |
|      10 | 0x1DC6      |        7622 |
|      11 | 0x1DC7      |        7623 |

## String References

- **7549**: <Sigh> When I sawy the falling stary the other day I made a wishy. I wishyed that Principal Koru-Moru would stoppy acting like a baby and get overy his stubbornness.
- **7589**: A burnite shelly...? Where have I heardy that namey beforey...?
- **7590**: Oh, I knowy! Doctor Yoran-Oran once mentionedy it, I thinky.
- **7622**: Why don't you try asking the othery professors abouty this "alchemy"?
- **7623**: One of them mighty be secretly researching it!
- **7886**: According to Principal Koru-Moru, there was once a great beasty that occasionally appeared in Sarutabaruta and ate any Tarutaru who happenedy to wandery by.
- **7887**: I'm sure gladdy I livey in an age when such beasties no longer existy!

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

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0030 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  00 80 1F 00 02 80 03 80         2........
0040: 04 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-81.879*, Z=124.072*, Y=-5.618*
  2: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0044 [0x00] END_REQSTACK()
```

### Event 293

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 26 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                29 08 23  F0 0E 01 01 1D 05 80 23       ).#.......#
0050: 1D 06 80 23 29 08 23 F0  0E 01 02 20 00 21 00     ...#).#.... .!. 
```

#### Opcodes

```
  0: 0x0045 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Maan-Pokuun (ID: 17756195/0x010EF023), tag_num=0x01)
  1: 0x004C [0x1D] PRINT_EVENT_MESSAGE(message_id=7886*)
    → "According to Principal Koru-Moru, there was once a great beasty that occasionally appeared in Sarutabaruta and ate any Tarutaru who happenedy to wandery by."
  2: 0x004F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=7887*)
    → "I'm sure gladdy I livey in an age when such beasties no longer existy!"
  4: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0054 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Maan-Pokuun (ID: 17756195/0x010EF023), tag_num=0x02)
  6: 0x005B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x005D [0x21] END_EVENT
  8: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               00                 .
```

#### Opcodes

```
  0: 0x005F [0x00] END_REQSTACK()
```

### Event 201

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 1E F0 FF FF 7F 6F 70 29  08 23 F0 0E 01 01 1D 07  .....op).#......
0070: 80 23 29 08 23 F0 0E 01  02 20 00 21 00           .#).#.... .!.   
```

#### Opcodes

```
  0: 0x0060 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0065 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0066 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0067 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Maan-Pokuun (ID: 17756195/0x010EF023), tag_num=0x01)
  4: 0x006E [0x1D] PRINT_EVENT_MESSAGE(message_id=7549*)
    → "<Sigh> When I sawy the falling stary the other day I made a wishy. I wishyed that Principal Koru-Moru would stoppy acting like a baby and get overy his stubbornness."
  5: 0x0071 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0072 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Maan-Pokuun (ID: 17756195/0x010EF023), tag_num=0x02)
  7: 0x0079 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x007B [0x21] END_EVENT
  9: 0x007C [0x00] END_REQSTACK()
```

### Event 220

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         1E F0 FF               ...
0080: FF 7F 6F 70 29 08 23 F0  0E 01 01 1D 08 80 23 1D  ..op).#.......#.
0090: 09 80 23 29 08 23 F0 0E  01 02 20 00 21 00        ..#).#.... .!.  
```

#### Opcodes

```
  0: 0x007D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0082 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0083 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0084 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Maan-Pokuun (ID: 17756195/0x010EF023), tag_num=0x01)
  4: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=7589*)
    → "A burnite shelly...? Where have I heardy that namey beforey...?"
  5: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=7590*)
    → "Oh, I knowy! Doctor Yoran-Oran once mentionedy it, I thinky."
  7: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0093 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Maan-Pokuun (ID: 17756195/0x010EF023), tag_num=0x02)
  9: 0x009A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x009C [0x21] END_EVENT
 11: 0x009D [0x00] END_REQSTACK()
```

### Event 230

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            1E F0                ..
00A0: FF FF 7F 6F 70 29 08 23  F0 0E 01 01 1D 0A 80 23  ...op).#.......#
00B0: 1D 0B 80 23 29 08 23 F0  0E 01 02 20 00 21 00     ...#).#.... .!. 
```

#### Opcodes

```
  0: 0x009E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00A4 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00A5 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Maan-Pokuun (ID: 17756195/0x010EF023), tag_num=0x01)
  4: 0x00AC [0x1D] PRINT_EVENT_MESSAGE(message_id=7622*)
    → "Why don't you try asking the othery professors abouty this "alchemy"?"
  5: 0x00AF [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00B0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7623*)
    → "One of them mighty be secretly researching it!"
  7: 0x00B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00B4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Maan-Pokuun (ID: 17756195/0x010EF023), tag_num=0x02)
  9: 0x00BB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00BD [0x21] END_EVENT
 11: 0x00BE [0x00] END_REQSTACK()
```
