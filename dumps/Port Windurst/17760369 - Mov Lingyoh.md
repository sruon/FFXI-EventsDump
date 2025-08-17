# 17760369 - Mov Lingyoh

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 132 bytes               |
| Total Events     | 5                       |
| References Count | 3                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [345](#event-345)        | 0x0030       |     35 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x001E      |          30 |
|       2 | 0x1006      |        4102 |

## String References

- **4102**: I was invited to join the secrrret meeting behind the warrrehouses, but I can't find them. What's a girrrl to do?

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
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

### Event 345

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 35 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 86 00 F8 FF FF 7F 1E F0  FF FF 7F 6F 70 29 08 71  ...........op).q
0040: 00 0F 01 01 1D 02 80 23  29 08 71 00 0F 01 02 20  .......#).q.... 
0050: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0030 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0036 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x003C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x003D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mov Lingyoh (ID: 17760369/0x010F0071), tag_num=0x01)
  5: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=4102*)
    → "I was invited to join the secrrret meeting behind the warrrehouses, but I can't find them. What's a girrrl to do?"
  6: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0048 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mov Lingyoh (ID: 17760369/0x010F0071), tag_num=0x02)
  8: 0x004F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0051 [0x21] END_EVENT
 10: 0x0052 [0x00] END_REQSTACK()
```
