# 17735701 - Nbu Latteh

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 96 bytes               |
| Total Events     | 3                      |
| References Count | 7                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [96](#event-96)          | 0x0001       |     12 |              3 |
| [65535.1](#event-655351) | 0x000D       |     24 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFFA87  |  4294965895 |
|       1 | 0xFFFFE7D8  |  4294961112 |
|       2 | 0x1B57      |        6999 |
|       3 | 0x0824      |        2084 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFFE161  |  4294959457 |
|       6 | 0xFFFFE5BB  |  4294960571 |

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

### Event 96

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 22 00 00            7........"..   
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.401*, z=-6.184*, y=6.999*, direction=183.2°*
  1: 0x000A [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 24 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         22 00 32               ".2
0010: 04 80 1F 00 05 80 06 80  02 80 1F 01 6F 1E 14 A0  ............o...
0020: 0E 01 6F 70 00                                    ..op.           
```

#### Opcodes

```
  0: 0x000D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.839*, Z=-6.725*, Y=6.999*
  3: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x001D [0x1E] EventEntity looks at Roh Latteh (ID: 17735700/0x010EA014) and starts talking
  6: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0023 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x0024 [0x00] END_REQSTACK()
```
