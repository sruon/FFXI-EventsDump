# 17756239 - Karija-Marija

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 176 bytes                |
| Total Events     | 6                        |
| References Count | 6                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [317](#event-317)        | 0x0021       |     39 |             13 |
| [336](#event-336)        | 0x0048       |     39 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1EFA      |        7930 |
|       3 | 0x1EFB      |        7931 |
|       4 | 0x1F1F      |        7967 |
|       5 | 0x1F20      |        7968 |

## String References

- **7930**: The Star Reading ceremony is a special rite that entails the gathering of the five ministers and the Star Sibyl together to listen-wisten to the will of the stars in the skies above. The last Star Reading said that Windurst would have everlasting peace-weace.
- **7931**: I'm just glad-wad we didn't have an ill-boding omen come up, like the ones we got during the Great War twenty years ago.
- **7967**: The Star Reading ceremony is a special rite that entails the gathering of the five ministers and the Star Sibyl together to listen-wisten to the will of the stars in the skies above.
- **7968**: The last few years' Star Reading-weadings didn't say much either way...neither good omens, nor bad.

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

### Event 317

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    86 00 F8 FF FF 7F 1E  F0 FF FF 7F 6F 70 29 0B   ...........op).
0030: 4F F0 0E 01 01 1D 02 80  23 1D 03 80 23 29 0B 4F  O.......#...#).O
0040: F0 0E 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0021 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0027 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x002D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x002E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Karija-Marija (ID: 17756239/0x010EF04F), tag_num=0x01)
  5: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7930*)
    → "The Star Reading ceremony is a special rite that entails the gathering of the five ministers and the Star Sibyl together to listen-wisten to the will of the stars in the skies above. The last Star Reading said that Windurst would have everlasting peace-weace."
  6: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=7931*)
    → "I'm just glad-wad we didn't have an ill-boding omen come up, like the ones we got during the Great War twenty years ago."
  8: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x003D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Karija-Marija (ID: 17756239/0x010EF04F), tag_num=0x02)
 10: 0x0044 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0046 [0x21] END_EVENT
 12: 0x0047 [0x00] END_REQSTACK()
```

### Event 336

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          86 00 F8 FF FF 7F 1E F0          ........
0050: FF FF 7F 6F 70 29 0B 4F  F0 0E 01 01 1D 04 80 23  ...op).O.......#
0060: 1D 05 80 23 29 0B 4F F0  0E 01 02 20 00 21 00     ...#).O.... .!. 
```

#### Opcodes

```
  0: 0x0048 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x004E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0054 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0055 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Karija-Marija (ID: 17756239/0x010EF04F), tag_num=0x01)
  5: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=7967*)
    → "The Star Reading ceremony is a special rite that entails the gathering of the five ministers and the Star Sibyl together to listen-wisten to the will of the stars in the skies above."
  6: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=7968*)
    → "The last few years' Star Reading-weadings didn't say much either way...neither good omens, nor bad."
  8: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0064 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Karija-Marija (ID: 17756239/0x010EF04F), tag_num=0x02)
 10: 0x006B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x006D [0x21] END_EVENT
 12: 0x006E [0x00] END_REQSTACK()
```
