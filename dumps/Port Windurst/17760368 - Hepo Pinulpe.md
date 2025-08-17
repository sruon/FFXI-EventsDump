# 17760368 - Hepo Pinulpe

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 136 bytes               |
| Total Events     | 5                       |
| References Count | 4                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [346](#event-346)        | 0x0030       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x1007      |        4103 |
|       3 | 0x1008      |        4104 |

## String References

- **4103**: On the otherrr side of this ocean therrre is a small harborrr town that is the homeland of us Mithra. My motherrr and sisterrr still live therrre.
- **4104**: But I chose to obey the voice of naturrre and jourrrney out into the unknown as a warriorrr. Even though I pine for my homeland, I know I probably will neverrr set foot on its ground everrr again...

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

### Event 346

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 29  08 70 00 0F 01 01 1D 02  .....op).p......
0040: 80 23 1D 03 80 23 29 08  70 00 0F 01 02 20 00 21  .#...#).p.... .!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hepo Pinulpe (ID: 17760368/0x010F0070), tag_num=0x01)
  4: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=4103*)
    → "On the otherrr side of this ocean therrre is a small harborrr town that is the homeland of us Mithra. My motherrr and sisterrr still live therrre."
  5: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=4104*)
    → "But I chose to obey the voice of naturrre and jourrrney out into the unknown as a warriorrr. Even though I pine for my homeland, I know I probably will neverrr set foot on its ground everrr again..."
  7: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0046 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hepo Pinulpe (ID: 17760368/0x010F0070), tag_num=0x02)
  9: 0x004D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x004F [0x21] END_EVENT
 11: 0x0050 [0x00] END_REQSTACK()
```
