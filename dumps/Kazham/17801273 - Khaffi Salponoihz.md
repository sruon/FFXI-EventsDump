# 17801273 - Khaffi Salponoihz

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 244 bytes        |
| Total Events     | 7                |
| References Count | 10               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [83](#event-83)          | 0x001A       |     33 |             12 |
| [176](#event-176)        | 0x003B       |     33 |             12 |
| [70](#event-70)          | 0x005C       |     33 |             12 |
| [73](#event-73)          | 0x007D       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x271C      |       10012 |
|       3 | 0x271D      |       10013 |
|       4 | 0x2874      |       10356 |
|       5 | 0x2875      |       10357 |
|       6 | 0x2747      |       10055 |
|       7 | 0x2748      |       10056 |
|       8 | 0x274C      |       10060 |
|       9 | 0x274D      |       10061 |

## String References

- **10012**: What's wrrrong, young adventurer? You look like you've got something on your mind.
- **10013**: Whenever something's trrroubling me, I sit back and relax in the Kazham sun, and everything is fine.
- **10055**: Oh, so you're going to grrreet the guardian of this island? Well, you're going to need some $2 to get up the volcano.
- **10056**: Once you've made the offering and been accepted by our guardian, you will be one of us. That is, if you come back alive.
- **10060**: The guardian has hearrrd your voice and accepted you. You're now one of us!
- **10061**: Enjoy the rest of your stay in our lush paradise of Kazham!
- **10356**: I'm going to give you two choices, and then I'm going to give you to the count of ten.
- **10357**: You can pack up and leave Kazham right now...or you can find some way of getting rrrid of that stench!

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
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

### Event 83

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 29 08 39 A0 0F 01 01  1D 02 80 23 1D 03 80 23  p).9.......#...#
0030: 29 08 39 A0 0F 01 02 20  00 21 00                 ).9.... .!.     
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khaffi Salponoihz (ID: 17801273/0x010FA039), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=10012*)
    → "What's wrrrong, young adventurer? You look like you've got something on your mind."
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=10013*)
    → "Whenever something's trrroubling me, I sit back and relax in the Kazham sun, and everything is fine."
  7: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0030 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khaffi Salponoihz (ID: 17801273/0x010FA039), tag_num=0x02)
  9: 0x0037 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0039 [0x21] END_EVENT
 11: 0x003A [0x00] END_REQSTACK()
```

### Event 176

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   1E F0 FF FF 7F             .....
0040: 6F 70 29 08 39 A0 0F 01  01 1D 04 80 23 1D 05 80  op).9.......#...
0050: 23 29 08 39 A0 0F 01 02  20 00 21 00              #).9.... .!.    
```

#### Opcodes

```
  0: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0041 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0042 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khaffi Salponoihz (ID: 17801273/0x010FA039), tag_num=0x01)
  4: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=10356*)
    → "I'm going to give you two choices, and then I'm going to give you to the count of ten."
  5: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=10357*)
    → "You can pack up and leave Kazham right now...or you can find some way of getting rrrid of that stench!"
  7: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0051 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khaffi Salponoihz (ID: 17801273/0x010FA039), tag_num=0x02)
  9: 0x0058 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x005A [0x21] END_EVENT
 11: 0x005B [0x00] END_REQSTACK()
```

### Event 70

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      1E F0 FF FF              ....
0060: 7F 6F 70 29 08 39 A0 0F  01 01 1D 06 80 23 1D 07  .op).9.......#..
0070: 80 23 29 08 39 A0 0F 01  02 20 00 21 00           .#).9.... .!.   
```

#### Opcodes

```
  0: 0x005C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0062 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0063 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khaffi Salponoihz (ID: 17801273/0x010FA039), tag_num=0x01)
  4: 0x006A [0x1D] PRINT_EVENT_MESSAGE(message_id=10055*)
    → "Oh, so you're going to grrreet the guardian of this island? Well, you're going to need some $2 to get up the volcano."
  5: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x006E [0x1D] PRINT_EVENT_MESSAGE(message_id=10056*)
    → "Once you've made the offering and been accepted by our guardian, you will be one of us. That is, if you come back alive."
  7: 0x0071 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0072 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khaffi Salponoihz (ID: 17801273/0x010FA039), tag_num=0x02)
  9: 0x0079 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x007B [0x21] END_EVENT
 11: 0x007C [0x00] END_REQSTACK()
```

### Event 73

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
0080: FF 7F 6F 70 29 08 39 A0  0F 01 01 1D 08 80 23 1D  ..op).9.......#.
0090: 09 80 23 29 08 39 A0 0F  01 02 20 00 21 00        ..#).9.... .!.  
```

#### Opcodes

```
  0: 0x007D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0082 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0083 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0084 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khaffi Salponoihz (ID: 17801273/0x010FA039), tag_num=0x01)
  4: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=10060*)
    → "The guardian has hearrrd your voice and accepted you. You're now one of us!"
  5: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=10061*)
    → "Enjoy the rest of your stay in our lush paradise of Kazham!"
  7: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0093 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khaffi Salponoihz (ID: 17801273/0x010FA039), tag_num=0x02)
  9: 0x009A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x009C [0x21] END_EVENT
 11: 0x009D [0x00] END_REQSTACK()
```
