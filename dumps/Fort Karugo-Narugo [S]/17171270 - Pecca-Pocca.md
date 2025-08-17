# 17171270 - Pecca-Pocca

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 164 bytes                       |
| Total Events     | 3                               |
| References Count | 6                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [233](#event-233)     | 0x0001       |     11 |              5 |
| [234](#event-234)     | 0x000C       |     97 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x200C      |        8204 |
|       1 | 0x200D      |        8205 |
|       2 | 0x0151      |         337 |
|       3 | 0x200E      |        8206 |
|       4 | 0x200F      |        8207 |
|       5 | 0x2010      |        8208 |

## String References

- **8204**: Did you catch a whiff of that smelly-welly flower monstaru lurking outside of here? I'm researching an all-new incense that'll out-stink it.
- **8205**: <Sniff, sniff> You smell just like an incense I make. You've metaru my friend, haven't you?
- **8206**: Hey, could you do me an itsy-bitsy teenie-weenie favor? Could you take this and give it to my friend next time you're headed for the Eldieme Necropolis?
- **8207**: I'd much rather go and offer the incense myself, but the living need attention too, you know. We wouldn't wantaru too many souls to pray for now, would we?
- **8208**: It's the next best thingy-wingy I can do, so make sure my friend gets the incense, okay? Thanks for helping outaru!

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

### Event 233

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8204*)
    → "Did you catch a whiff of that smelly-welly flower monstaru lurking outside of here? I'm researching an all-new incense that'll out-stink it."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 234

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 97 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      42 1E F0 FF              B...
0010: FF 7F 1D 01 80 23 6F 70  5B 02 80 F8 FF FF 7F F8  .....#op[.......
0020: FF FF 7F 74 6C 6B 30 1D  03 80 23 1D 04 80 23 5B  ...tlk0...#...#[
0030: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 31 5B 02 80 F8 FF  .......tlk1[....
0050: FF 7F F8 FF FF 7F 77 61  69 30 1D 05 80 23 53 F8  ......wai0...#S.
0060: FF FF 7F F8 FF FF 7F 77  61 69 30 21 00           .......wai0!.   
```

#### Opcodes

```
  0: 0x000C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=8205*)
    → "<Sniff, sniff> You smell just like an incense I make. You've metaru my friend, haven't you?"
  3: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0016 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0017 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0018 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=337*
  7: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=8206*)
    → "Hey, could you do me an itsy-bitsy teenie-weenie favor? Could you take this and give it to my friend next time you're headed for the Eldieme Necropolis?"
  8: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=8207*)
    → "I'd much rather go and offer the incense myself, but the living need attention too, you know. We wouldn't wantaru too many souls to pray for now, would we?"
 10: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x002F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=337*
 12: 0x003E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 13: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wai0" with entities [EventEntity, EventEntity], work=337*
 14: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=8208*)
    → "It's the next best thingy-wingy I can do, so make sure my friend gets the incense, okay? Thanks for helping outaru!"
 15: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x005E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wai0" with entities [EventEntity, EventEntity]
 17: 0x006B [0x21] END_EVENT
 18: 0x006C [0x00] END_REQSTACK()
```
