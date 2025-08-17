# 17756245 - Malmi-Monmi

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 180 bytes                |
| Total Events     | 6                        |
| References Count | 11                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [65535.3](#event-655353) | 0x0021       |     23 |              5 |
| [295](#event-295)        | 0x0038       |     39 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFEB6C4  |  4294883012 |
|       3 | 0x204A3     |      132259 |
|       4 | 0xFFFFEB80  |  4294962048 |
|       5 | 0x0530      |        1328 |
|       6 | 0xFFFEBD4B  |  4294884683 |
|       7 | 0x1EF8B     |      126859 |
|       8 | 0xFFFFEB9A  |  4294962074 |
|       9 | 0x1ED4      |        7892 |
|      10 | 0x1ED5      |        7893 |

## String References

- **7892**: Windurst Walls is the coolest-woolest place. Not only do we have Heavens Tower and a consulate, but all the ex-ministers have manors here!
- **7893**: When the ministers of the five magic ministries of Windurst retire, they gain the title of doctor or professor, and are allowed to live in special-wecial houses so they can continue their studies without worries.

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
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 00 80 37 02 80 03  80 04 80 05 80 1F 00 06   2..7...........
0030: 80 07 80 08 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0024 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-84.284*, z=132.259*, y=-5.248*, direction=116.7°*
  2: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=-82.613*, Z=126.859*, Y=-5.222*
  3: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0037 [0x00] END_REQSTACK()
```

### Event 295

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          86 00 F8 FF FF 7F 1E F0          ........
0040: FF FF 7F 6F 70 29 0B 55  F0 0E 01 01 1D 09 80 23  ...op).U.......#
0050: 1D 0A 80 23 29 0B 55 F0  0E 01 02 20 00 21 00     ...#).U.... .!. 
```

#### Opcodes

```
  0: 0x0038 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x003E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0043 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0044 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0045 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Malmi-Monmi (ID: 17756245/0x010EF055), tag_num=0x01)
  5: 0x004C [0x1D] PRINT_EVENT_MESSAGE(message_id=7892*)
    → "Windurst Walls is the coolest-woolest place. Not only do we have Heavens Tower and a consulate, but all the ex-ministers have manors here!"
  6: 0x004F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=7893*)
    → "When the ministers of the five magic ministries of Windurst retire, they gain the title of doctor or professor, and are allowed to live in special-wecial houses so they can continue their studies without worries."
  8: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0054 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Malmi-Monmi (ID: 17756245/0x010EF055), tag_num=0x02)
 10: 0x005B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x005D [0x21] END_EVENT
 12: 0x005E [0x00] END_REQSTACK()
```
