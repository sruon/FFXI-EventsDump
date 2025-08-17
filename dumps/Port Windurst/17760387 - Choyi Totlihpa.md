# 17760387 - Choyi Totlihpa

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 176 bytes               |
| Total Events     | 5                       |
| References Count | 7                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [215](#event-215)        | 0x001A       |     33 |             12 |
| [622](#event-622)        | 0x003B       |     52 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0166      |         358 |
|       1 | 0x001E      |          30 |
|       2 | 0x0E29      |        3625 |
|       3 | 0x0E2A      |        3626 |
|       4 | 0x3321      |       13089 |
|       5 | 0x3325      |       13093 |
|       6 | 0x3326      |       13094 |

## String References

- **3625**: The porrrt district, by its very naturrre, has a lot of people coming and going all the time, so the chances of meeting up with bad company is greaterrr.
- **3626**: Don't let the frrresh sea brrreeze get to your head. Keep yourrr wits about you always!
- **13089**: <Player>'s badge flashes brightly.
- **13093**: Have you seen anyone from the mercenary company yet? Apparently, they'rrre from the "Empire of Aht Urhgan."
- **13094**: You may think they seem trrrustworthy, but take my word for it--with a face like that, they've just gotta be thinking criminal thoughts. You'd best be carrreful.

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=358*
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

### Event 215

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
0020: 70 29 08 83 00 0F 01 01  1D 02 80 23 1D 03 80 23  p).........#...#
0030: 29 08 83 00 0F 01 02 20  00 21 00                 )...... .!.     
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choyi Totlihpa (ID: 17760387/0x010F0083), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=3625*)
    → "The porrrt district, by its very naturrre, has a lot of people coming and going all the time, so the chances of meeting up with bad company is greaterrr."
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=3626*)
    → "Don't let the frrresh sea brrreeze get to your head. Keep yourrr wits about you always!"
  7: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0030 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Choyi Totlihpa (ID: 17760387/0x010F0083), tag_num=0x02)
  9: 0x0037 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0039 [0x21] END_EVENT
 11: 0x003A [0x00] END_REQSTACK()
```

### Event 622

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   42 48 04 80 1E             BH...
0040: F0 FF FF 7F 1C 01 80 1D  05 80 23 5B 00 80 F8 FF  ..........#[....
0050: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 06 80 23 5B 00  ......tlk0...#[.
0060: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 21 00     .........tlk1!. 
```

#### Opcodes

```
  0: 0x003B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x003C [0x48] [System] [13089*]:
    → "<Player>'s badge flashes brightly."
  2: 0x003F [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0044 [0x1C] WAIT(30* ticks)
  4: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=13093*)
    → "Have you seen anyone from the mercenary company yet? Apparently, they'rrre from the "Empire of Aht Urhgan.""
  5: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=358*
  7: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=13094*)
    → "You may think they seem trrrustworthy, but take my word for it--with a face like that, they've just gotta be thinking criminal thoughts. You'd best be carrreful."
  8: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x005E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=358*
 10: 0x006D [0x21] END_EVENT
 11: 0x006E [0x00] END_REQSTACK()
```
