# 17752092 - Mejina-Monjina

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 308 bytes                 |
| Total Events     | 9                         |
| References Count | 11                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [282](#event-282)        | 0x0030       |     29 |             10 |
| [286](#event-286)        | 0x004D       |     33 |             12 |
| [290](#event-290)        | 0x006E       |     33 |             12 |
| [294](#event-294)        | 0x008F       |     33 |             12 |
| [298](#event-298)        | 0x00B0       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1F1D      |        7965 |
|       3 | 0x1F26      |        7974 |
|       4 | 0x1F27      |        7975 |
|       5 | 0x1F33      |        7987 |
|       6 | 0x1F34      |        7988 |
|       7 | 0x1F3C      |        7996 |
|       8 | 0x1F3D      |        7997 |
|       9 | 0x1F45      |        8005 |
|      10 | 0x1F46      |        8006 |

## String References

- **7965**: Every star has its own name, just like we do! Doesn't that just make you have a closer affinity with them?
- **7974**: The three telescopes found here are hundreds of years old and have become rather antiquated.
- **7975**: Many a time there's been talk of rebuilding them, but we've not been able to do it yet.
- **7987**: In olden days, pirates used the ancient Tarutaru money, which had the constellations drawn on them, to help them navigate by the stars...or so the folktales go.
- **7988**: But now that most of the open seas have been charted into set shipping routes, they don't need $2 anymore.
- **7996**: How did you manage to get your hands on $2? I never thought we'd see one of those again!
- **7997**: Oh, I see... Wa-ha-ha! Those old buccaneers had some hidden away, eh? Even pirates come in useful at times too, huh?
- **8005**: The real classical Tarutaru money has Odin drawn to the north, of course.
- **8006**: You can'taru go having Odin on the east or west now, can you?

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

### Event 282

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 29  08 1C E0 0E 01 01 1D 02  .....op)........
0040: 80 23 29 08 1C E0 0E 01  02 20 00 21 00           .#)...... .!.   
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x01)
  4: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=7965*)
    → "Every star has its own name, just like we do! Doesn't that just make you have a closer affinity with them?"
  5: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0042 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x02)
  7: 0x0049 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x004B [0x21] END_EVENT
  9: 0x004C [0x00] END_REQSTACK()
```

### Event 286

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         1E F0 FF               ...
0050: FF 7F 6F 70 29 08 1C E0  0E 01 01 1D 03 80 23 1D  ..op).........#.
0060: 04 80 23 29 08 1C E0 0E  01 02 20 00 21 00        ..#)...... .!.  
```

#### Opcodes

```
  0: 0x004D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0052 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0053 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0054 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x01)
  4: 0x005B [0x1D] PRINT_EVENT_MESSAGE(message_id=7974*)
    → "The three telescopes found here are hundreds of years old and have become rather antiquated."
  5: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=7975*)
    → "Many a time there's been talk of rebuilding them, but we've not been able to do it yet."
  7: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0063 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x02)
  9: 0x006A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x006C [0x21] END_EVENT
 11: 0x006D [0x00] END_REQSTACK()
```

### Event 290

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            1E F0                ..
0070: FF FF 7F 6F 70 29 08 1C  E0 0E 01 01 1D 05 80 23  ...op).........#
0080: 1D 06 80 23 29 08 1C E0  0E 01 02 20 00 21 00     ...#)...... .!. 
```

#### Opcodes

```
  0: 0x006E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0073 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0074 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0075 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x01)
  4: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=7987*)
    → "In olden days, pirates used the ancient Tarutaru money, which had the constellations drawn on them, to help them navigate by the stars...or so the folktales go."
  5: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=7988*)
    → "But now that most of the open seas have been charted into set shipping routes, they don't need $2 anymore."
  7: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0084 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x02)
  9: 0x008B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x008D [0x21] END_EVENT
 11: 0x008E [0x00] END_REQSTACK()
```

### Event 294

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               1E                 .
0090: F0 FF FF 7F 6F 70 29 08  1C E0 0E 01 01 1D 07 80  ....op).........
00A0: 23 1D 08 80 23 29 08 1C  E0 0E 01 02 20 00 21 00  #...#)...... .!.
```

#### Opcodes

```
  0: 0x008F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0094 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0095 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0096 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x01)
  4: 0x009D [0x1D] PRINT_EVENT_MESSAGE(message_id=7996*)
    → "How did you manage to get your hands on $2? I never thought we'd see one of those again!"
  5: 0x00A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7997*)
    → "Oh, I see... Wa-ha-ha! Those old buccaneers had some hidden away, eh? Even pirates come in useful at times too, huh?"
  7: 0x00A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00A5 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x02)
  9: 0x00AC [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00AE [0x21] END_EVENT
 11: 0x00AF [0x00] END_REQSTACK()
```

### Event 298

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 1E F0 FF FF 7F 6F 70 29  08 1C E0 0E 01 01 1D 09  .....op)........
00C0: 80 23 1D 0A 80 23 29 08  1C E0 0E 01 02 20 00 21  .#...#)...... .!
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B0 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B6 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00B7 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x01)
  4: 0x00BE [0x1D] PRINT_EVENT_MESSAGE(message_id=8005*)
    → "The real classical Tarutaru money has Odin drawn to the north, of course."
  5: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=8006*)
    → "You can'taru go having Odin on the east or west now, can you?"
  7: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00C6 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mejina-Monjina (ID: 17752092/0x010EE01C), tag_num=0x02)
  9: 0x00CD [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00CF [0x21] END_EVENT
 11: 0x00D0 [0x00] END_REQSTACK()
```
