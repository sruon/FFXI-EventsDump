# 17801218 - Khau Mahiyoeloh

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 176 bytes        |
| Total Events     | 7                |
| References Count | 5                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [60](#event-60)          | 0x001A       |     33 |             12 |
| [165](#event-165)        | 0x003B       |     29 |             10 |
| [313](#event-313)        | 0x0058       |     12 |              3 |
| [315](#event-315)        | 0x0064       |     12 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x26FA      |        9978 |
|       3 | 0x26FB      |        9979 |
|       4 | 0x2861      |       10337 |

## String References

- **9978**: You headed to the Yuhtunga Jungle? On the east side there's a volcano. Inside that volcano is Ifrit's Cauldron. I wouldn't rrrecommend any sightseeing tours. Those places are pretty nasty.
- **9979**: Also, on the far southeastern side of this island is an ancient, rrrundown temple. Not many live to see it, though. The jungles here are teeming with vicious beasts...
- **10337**: Oh my g... What IS that smell!? Get out of here before we're rrrevisited by those Elshimo frogs I had for lunch!

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

### Event 60

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
0020: 70 29 08 02 A0 0F 01 01  1D 02 80 23 1D 03 80 23  p).........#...#
0030: 29 08 02 A0 0F 01 02 20  00 21 00                 )...... .!.     
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khau Mahiyoeloh (ID: 17801218/0x010FA002), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=9978*)
    → "You headed to the Yuhtunga Jungle? On the east side there's a volcano. Inside that volcano is Ifrit's Cauldron. I wouldn't rrrecommend any sightseeing tours. Those places are pretty nasty."
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=9979*)
    → "Also, on the far southeastern side of this island is an ancient, rrrundown temple. Not many live to see it, though. The jungles here are teeming with vicious beasts..."
  7: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0030 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khau Mahiyoeloh (ID: 17801218/0x010FA002), tag_num=0x02)
  9: 0x0037 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0039 [0x21] END_EVENT
 11: 0x003A [0x00] END_REQSTACK()
```

### Event 165

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   1E F0 FF FF 7F             .....
0040: 6F 70 29 08 02 A0 0F 01  01 1D 04 80 23 29 08 02  op).........#)..
0050: A0 0F 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0041 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0042 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khau Mahiyoeloh (ID: 17801218/0x010FA002), tag_num=0x01)
  4: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=10337*)
    → "Oh my g... What IS that smell!? Get out of here before we're rrrevisited by those Elshimo frogs I had for lunch!"
  5: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khau Mahiyoeloh (ID: 17801218/0x010FA002), tag_num=0x02)
  7: 0x0054 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0056 [0x21] END_EVENT
  9: 0x0057 [0x00] END_REQSTACK()
```

### Event 313

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          92 01 F8 FF FF 7F 80 F8          ........
0060: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0058 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005E [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0063 [0x00] END_REQSTACK()
```

### Event 315

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             92 01 F8 FF  FF 7F 80 F8 FF FF 7F 00      ............
```

#### Opcodes

```
  0: 0x0064 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006A [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x006F [0x00] END_REQSTACK()
```
