# 17756226 - Suhie-Kaihie

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 192 bytes                |
| Total Events     | 8                        |
| References Count | 11                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [65535.3](#event-655353) | 0x0021       |     10 |              2 |
| [65535.4](#event-655354) | 0x002B       |     14 |              4 |
| [291](#event-291)        | 0x0039       |     39 |             13 |
| [65535.5](#event-655355) | 0x0060       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFE779B  |  4294866843 |
|       3 | 0x23BFC     |      146428 |
|       4 | 0xFFFFEB79  |  4294962041 |
|       5 | 0x02DF      |         735 |
|       6 | 0xFFFEA6D1  |  4294878929 |
|       7 | 0x1F4CA     |      128202 |
|       8 | 0xFFFFEB85  |  4294962053 |
|       9 | 0x1ECA      |        7882 |
|      10 | 0x1ECB      |        7883 |

## String References

- **7882**: Hullo-wullo! Are you from Windurst yourselfy-welfy? Or are you just another adventurer passing throughy-woughy?
- **7883**: Either way, it's a dangerous place outside of this towny-wowny. If you intend on venturing outside, then you had better make sure your armor and weapons are properly equipped firsty-wirsty!

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

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    37 02 80 03 80 04 80  05 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0021 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-100.453*, z=146.428*, y=-5.255*, direction=64.6°*
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   32 00 80 1F 00             2....
0030: 06 80 07 80 08 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=-88.367*, Z=128.202*, Y=-5.243*
  2: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0038 [0x00] END_REQSTACK()
```

### Event 291

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             86 00 F8 FF FF 7F 1E           .......
0040: F0 FF FF 7F 6F 70 29 0B  42 F0 0E 01 01 1D 09 80  ....op).B.......
0050: 23 1D 0A 80 23 29 0B 42  F0 0E 01 02 20 00 21 00  #...#).B.... .!.
```

#### Opcodes

```
  0: 0x0039 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x003F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0045 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0046 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Suhie-Kaihie (ID: 17756226/0x010EF042), tag_num=0x01)
  5: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7882*)
    → "Hullo-wullo! Are you from Windurst yourselfy-welfy? Or are you just another adventurer passing throughy-woughy?"
  6: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=7883*)
    → "Either way, it's a dangerous place outside of this towny-wowny. If you intend on venturing outside, then you had better make sure your armor and weapons are properly equipped firsty-wirsty!"
  8: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0055 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Suhie-Kaihie (ID: 17756226/0x010EF042), tag_num=0x02)
 10: 0x005C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x005E [0x21] END_EVENT
 12: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0060 [0x00] END_REQSTACK()
```
